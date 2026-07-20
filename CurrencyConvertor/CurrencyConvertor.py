import requests


def get_exchange_rate(from_currency, to_currency):

    url = f"https://api.frankfurter.app/latest"
    params = {
        "from": from_currency.upper(),
        "to": to_currency.upper()
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["rates"][to_currency.upper()]
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None
    except KeyError:
        print("Invalid currency code.")
        return None


def currency_converter(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return None
    return round(amount * rate, 2)


def main():
    print("Live Currency Converter (powered by frankfurter.app)")

    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g. USD): ").strip()
    to_currency = input("To currency (e.g. EUR): ").strip()

    result = currency_converter(amount, from_currency, to_currency)

    if result is None:
        print("Conversion failed. Check currency codes or your internet connection.")
    else:
        print(f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}")


if __name__ == "__main__":
    main()
