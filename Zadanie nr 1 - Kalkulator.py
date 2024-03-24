print("Witamy w programie - Kalkulator")
a = float(input("Podaj pierwszą liczbę, którą chcesz obliczyć "))
b = float(input("Podaj drugą liczbę, którą chcesz obliczyć "))

print()
while True:
    c = int(input("Wybierz opcje poprzez podanie odpowiedniej cyfry:\n1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie\n"))
    if c < 1 or c > 5: 
        print("Wybrano złą opcję spróbuj jeszcze raz")
    else:
        break
if c==1:
    print("Wybrano dodawanie")
    wynik = float(a+b)
    print("Wynik dodawania liczby a =", a, "i liczby b =", b, "wynosi : ",wynik)
elif c==2:
    print("Wybrano odejmowanie")
    wynik = float(a-b)
    print("Wynik odejmowania liczby a =", a, "i liczby b =", b, "wynosi : ",wynik)
elif c==3:
    print("Wybrano mnożenie")
    wynik = float(a*b)
    print("Wynik mnożenia liczby a =", a, "i liczby b =", b, "wynosi : ",round(wynik,2))
elif c==4:
    print("Wybrano dzielenie")
    wynik = float(a/b)
    print("Wynik dzielenia liczby a =", a, "i liczby b =", b, "wynosi : ",round(wynik,2)) 
        