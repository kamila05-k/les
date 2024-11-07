def convert_(amount, from_, to_, exchange_):
    if from_ not in exchange_ or to_ not in exchange_:
        raise ValueError("Белгиленген валюталар жок.")
    rate_from = exchange_[from_]
    rate_to = exchange_[to_]
    converted_amount = amount * (rate_to / rate_from)
    return converted_amount


exchange_rates = {
    "USD": 0.01333,
    "EUR": 0.01116,
    "RUB": 1.0
}
try:
    amount = float(input("Айландыруу үчүн сумманы киргизиңиз: "))
    from_currency = input("Баштапкы валютаны киргизиңиз (USD, EUR, RUB): ").upper()
    to_currency = input("Максаттуу валютаны киргизиңиз (USD, EUR, RUB): ").upper()
    convert_amount = convert_(amount, from_currency, to_currency, exchange_rates)
    print(f"{amount} {from_currency} == {convert_amount:.2f} {to_currency}.")
except ValueError as e:
    print("Ката кетти: ", e)
except Exception as e:
    print("Ката кетти: Негизги ката:", e)
