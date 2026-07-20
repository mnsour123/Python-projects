# Currency Converter

A simple Python command-line tool to convert between currencies using **live exchange rates** from the [Frankfurter API](https://www.frankfurter.app/) (no API key required).

## Features

- Convert any amount between supported currencies
- Uses real-time exchange rates (based on European Central Bank data)
- Simple command-line interface
- No API key or sign-up needed

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone or download this repository.
2. Install the required dependency:

   ```bash
   pip install requests
   ```

## Usage

Run the script from your terminal:

```bash
python currency_converter.py
```

You'll be prompted to enter:

1. The amount you want to convert
2. The currency you're converting **from** (e.g. `USD`)
3. The currency you're converting **to** (e.g. `EUR`)

### Example

```
Live Currency Converter (powered by frankfurter.app)
Enter amount: 100
From currency (e.g. USD): USD
To currency (e.g. EUR): EUR
100.0 USD = 92.15 EUR
```

## Supported Currencies

Any currency code supported by the Frankfurter API, including but not limited to:

`USD`, `EUR`, `GBP`, `JPY`, `INR`, `AUD`, `CAD`, `CHF`, `CNY`, `NZD`

See the full list at [frankfurter.app/currencies](https://www.frankfurter.app/currencies).

## How It Works

The script sends a request to:

```
https://api.frankfurter.app/latest?from=<FROM_CURRENCY>&to=<TO_CURRENCY>
```

It then parses the JSON response to retrieve the current exchange rate and calculates the converted amount.

## Error Handling

- Invalid currency codes will return an error message.
- Network issues (timeouts, no connection) are caught and reported without crashing the program.

## Possible Improvements

- [ ] Add offline mode with cached exchange rates
- [ ] Build a GUI version using `tkinter`
- [ ] Support batch conversions from a file
- [ ] Add historical exchange rate lookups

## License

This project is free to use and modify for personal or educational purposes.
