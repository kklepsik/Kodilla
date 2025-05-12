import sqlite3
from sqlite3 import Error

def create_connection(database):
    connection = None
    try:
        connection = sqlite3.connect(database)
        print(f"Connected to {database}, sqllite version: {sqlite3.version}")
        return connection
    except Error as error:
        print(error)
    return connection




def execute_sql(connection, sql_code):
    
    try:
        cursor = connection.cursor()
        cursor.execute(sql_code)

    except Error as error:
        print(error)


def add_train(connection, train):

    sql = '''INSERT INTO trains(name, cost, max_speed, country) VALUES(?,?,?,?)'''
    cursor = connection.cursor()
    cursor.execute(sql, train)      #executemany pozwala na dodawanie wielu wierszy
    connection.commit()
    return cursor.lastrowid

def add_route(connection, route):
    
    sql = '''INSERT INTO routes(train_id, start, stop) VALUES(?,?,?)'''
    cursor = connection.cursor()
    cursor.execute(sql, route) 
    connection.commit()
    return cursor.lastrowid


def select_all(connection, table):

    sql = f"SELECT * FROM {table}"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = (cursor.fetchall())
    print(rows)
    return rows                   #pobierz wszystkie
    
    

def update_row(connection, table, data, id):

    """
    Prosta funkcja do aktualizacji wiersza w tabeli SQL.
    connection: połączenie z bazą SQLite
    table: nazwa tabeli
    data: słownik z kolumnami i wartościami
    id: wartość ID wiersza do aktualizacji
    """

    cursor = connection.cursor()
    
    keys_for_change = [f"{key} = ?" for key in data]            #atrybuty do zmiany w formie sql
    print(keys_for_change)
    sql = f"UPDATE {table} SET {', '.join(keys_for_change)} WHERE id = ?"         #zapytanie
    print(sql)
    values = list(data.values()) + [id]
    print(values)

    try:
        cursor.execute(sql, values)
        connection.commit()
        return cursor.rowcount > 0
    except:
        return False


def delete_where(connection, table, **kwargs):
    """
    Prosta funkcja do usuwania wierszy z tabeli SQL na podstawie dowolnych warunków.
    connection: połączenie z bazą SQLite
    table: nazwa tabeli
    **kwargs: warunki w formacie kolumna=wartosc 
    """
    cursor = connection.cursor()
    conditions = []  # Lista fragmentów warunku, np. ["nazwa=?", "rok=?"]
    condition_values = []  # Lista wartości dla placeholderów, np. ["Fiat", 2020]

    # Budowanie warunków i wartości na podstawie kwargs
    for column, value in kwargs.items():
        conditions.append(f"{column}=?")
        condition_values.append(value)

    # Łączenie warunków znakiem AND
    conditions = " AND ".join(conditions)

    # Tworzenie zapytania SQL
    sql = f"DELETE FROM {table} WHERE {conditions}"

    try:
        cursor.execute(sql, condition_values)
        connection.commit()
        return cursor.rowcount > 0  # True, jeśli usunięto wiersze
    except:
        return False  # False w razie błędu



if __name__ == '__main__':
    # Połączenie z bazą
    database = "trains.db"
    connection = create_connection(database)

    if connection is not None:
        # Tworzenie tabel
        create_trains_sql = """
        CREATE TABLE IF NOT EXISTS trains (
            id INTEGER PRIMARY KEY,
            name TEXT,
            cost REAL,
            max_speed REAL,
            country TEXT
        )
        """

        create_routes_sql = """
        CREATE TABLE IF NOT EXISTS routes (
            id INTEGER PRIMARY KEY,
            train_id INTEGER,
            start TEXT,
            stop TEXT,
            FOREIGN KEY (train_id) REFERENCES trains(id)
        )
        """

        execute_sql(connection, create_trains_sql)
        execute_sql(connection, create_routes_sql)

        # Dodawanie danych
        train = ("FLIRT", 2000000, 200, "Polska")
        train_id = add_train(connection, train)

        route = (train_id, "Warszawa", "Kraków")
        route_id = add_route(connection, route)


        print(f"Added train with ID {train_id}")
        print(f"Added route with ID {route_id}")

        row = select_all(connection, "trains")
        data = {"name": "DART","cost": 3000000}
        update_row(connection, "trains", data, 5)

        row_deleted = delete_where(connection, "routes", id = 3)
        print(row_deleted)
    

        # Zamykanie połączenia
        connection.close()


   