def kalkulator(operacja):
    try:
        if "/" in operacja:
            _, druga_liczba = operacja.split("/")
            if float(druga_liczba) == 0:
                return "Nie dziel przez 0"
 wynik = eval(operacja)
        return wynik
    except Exception as e:
        return f"Błąd: {e}"

operacja = input("Wprowadź operację matematyczną (np. 3 + 2, 3*3): ")
wynik = kalkulator(operacja)
print(f"Wynik operacji {operacja} to: {wynik}")
