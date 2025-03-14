def shopping(items, payment='karta', shop='sklep osiedlowy'):
    result = ""
    result = result + f"Robię zakupy w {shop}. \n Kupuję następujące rzeczy: \n"
    for item in items:
        result = result + f"- {item} \n"
    result = result + f"Metoda płatności: {payment}"
    return result


if __name__ == "__main__":

    items = input("Lista zakupów z przecinkami:").split(', ')
    print(shopping(items))