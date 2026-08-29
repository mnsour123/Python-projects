import argparse
import csv
import sys
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; QuoteScraperBot/1.0)"}


def fetch_page(url: str) -> BeautifulSoup:
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def parse_quotes(soup: BeautifulSoup) -> list[dict]:
    quotes = []
    for block in soup.select(".quote"):
        text = block.select_one(".text").get_text(strip=True)
        author = block.select_one(".author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in block.select(".tags .tag")]
        quotes.append({"text": text, "author": author, "tags": ", ".join(tags)})
    return quotes


def scrape(max_pages: int | None = None, delay: float = 1.0) -> list[dict]:
    all_quotes = []
    page = 1
    url = BASE_URL

    while url:
        print(f"Scraping page {page}: {url}")
        soup = fetch_page(url)
        all_quotes.extend(parse_quotes(soup))

        if max_pages and page >= max_pages:
            break

        next_link = soup.select_one("li.next a")
        url = BASE_URL + next_link["href"] if next_link else None
        page += 1

        if url:
            time.sleep(delay)

    return all_quotes


def save_to_csv(quotes: list[dict], filename: str) -> None:
    """Write scraped quotes to a CSV file."""
    if not quotes:
        print("No quotes to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(quotes)

    print(f"Saved {len(quotes)} quotes to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Scrape quotes from quotes.toscrape.com")
    parser.add_argument("--pages", type=int, default=None, help="Max number of pages to scrape")
    parser.add_argument("--output", type=str, default="quotes.csv", help="Output CSV filename")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests (seconds)")
    args = parser.parse_args()

    try:
        quotes = scrape(max_pages=args.pages, delay=args.delay)
    except requests.RequestException as e:
        print(f"Error fetching page: {e}", file=sys.stderr)
        sys.exit(1)

    save_to_csv(quotes, args.output)


if __name__ == "__main__":
    main()
