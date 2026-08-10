# Quote Scraper

A small Python project that scrapes quotes, authors, and tags from
[quotes.toscrape.com](https://quotes.toscrape.com) — a site built
specifically for practicing web scraping — and saves the results to CSV.

## Project structure

```
quote-scraper/
├── scraper.py        # main scraper script
├── test_scraper.py   # unit tests (run offline, using a local HTML fixture)
├── requirements.txt  # dependencies
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Scrape every page:

```bash
python scraper.py
```

Scrape only the first 3 pages, save to a custom filename:

```bash
python scraper.py --pages 3 --output my_quotes.csv
```

Adjust the delay between requests (default 1 second, be polite to the server):

```bash
python scraper.py --delay 2
```

## Output

A CSV file with three columns: `text`, `author`, `tags`.

## Running tests

```bash
python test_scraper.py
```

Tests check the parsing logic against a local HTML fixture, so they don't
require network access.

## How it works

1. `fetch_page()` downloads a page with `requests` and parses it with
   `BeautifulSoup`.
2. `parse_quotes()` pulls out each quote's text, author, and tags using
   CSS selectors.
3. `scrape()` follows the "Next" link across pages until there isn't one
   (or until `--pages` is reached).
4. `save_to_csv()` writes everything to disk.

## Extending it

- Swap `BASE_URL` and the CSS selectors in `parse_quotes()` to target a
  different site.
- Add `--format json` to support JSON output alongside CSV.
- Add retry logic (e.g. with `requests`'s `Retry`/`HTTPAdapter`) for
  more robust scraping of flaky sites.
