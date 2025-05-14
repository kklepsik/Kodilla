from sqlalchemy import create_engine, Table, Column,Integer, String, MetaData
import pandas as pd

engine = create_engine('sqlite:///stations.db', echo = True)            #echo pokazuje wykonywanie kodu sql

#wczytanie danych
stacje = r"C:\Users\kkleps\Downloads\clean_stations.csv"
pomiary = r"C:\Users\kkleps\Downloads\clean_measure.csv"
stations = pd.read_csv(stacje)
measurments = pd.read_csv(pomiary)

stations.to_sql('stations', con=engine, if_exists = 'replace', index = False)
measurments.to_sql('measurments', con=engine, if_exists = 'replace', index = False)


with engine.connect() as conn:
    result = conn.execute("SELECT * FROM stations LIMIT 5")             #czym sie różni czy uzyje fetchall czy nie, zwraca to samo
    for row in result:
        print(row)