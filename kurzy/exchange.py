import httpx

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

response = httpx.get(URL)
text = response.text

lines = text.split("\n")

eur_rate = 0

for line in lines:
    columns = line.split("|")

    if len(columns) < 5:
        continue

    if columns[3] == "EUR":
        rate_text = columns[4]
        rate_text = rate_text.replace(",", ".")
        eur_rate = float(rate_text)
        break

print("Aktuální kurz EUR:", eur_rate)

choice = ""

while choice != "1" and choice != "2" and choice != "ITADORI":
    print("Zvol typ převodu:")
    print("1 - EUR -> CZK")
    print("2 - CZK -> EUR")
    choice = input("Volba: ")

    if choice != "1" and choice != "2" and choice != "ITADORI":
        print("Neplatná volba.\n")

amount = 0

while amount <= 0:
    try:
        amount = float(input("Částka: "))
        if amount <= 0:
            print("Částka musí být větší než 0.")
    except ValueError:
        print("Zadej číslo.")

if choice == "1":
    result = amount * eur_rate
    print(amount, "EUR =", round(result, 2), "CZK")
elif choice == "2":
    result = amount / eur_rate
    print(amount, "CZK =", round(result, 2), "EUR")
elif choice == "ITADORI":
    print("Y" + int(amount) * "U" + "JI")
else:
    print("Neplatná volba.")