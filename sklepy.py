def shopping(items, payment='karta', shop='sklep osiedlowy'):
    result = ""
    result = result + f"Robię zakupy w {shop}. \n Kupuję następujące rzeczy: \n"
    for item in items:
        result = result + f"- {item} \n"
    result = result + f"Metoda płatności: {payment}"
    return result

items = ["cola", "whiskey", "lód"]
text = shopping(items, 'card', 'small local shop')
print(text)