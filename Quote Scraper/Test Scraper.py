from bs4 import BeautifulSoup
from scraper import parse_quotes

SAMPLE_HTML = """
<html>
  <body>
    <div class="quote">
      <span class="text">"The world as we have created it is a process of our thinking."</span>
      <span>
        by <small class="author">Albert Einstein</small>
      </span>
      <div class="tags">
        <a class="tag">change</a>
        <a class="tag">deep-thoughts</a>
      </div>
    </div>
    <div class="quote">
      <span class="text">"It is our choices that show what we truly are."</span>
      <span>
        by <small class="author">J.K. Rowling</small>
      </span>
      <div class="tags">
        <a class="tag">choices</a>
      </div>
    </div>
  </body>
</html>
"""


def test_parse_quotes_extracts_all_quotes():
    soup = BeautifulSoup(SAMPLE_HTML, "html.parser")
    quotes = parse_quotes(soup)
    assert len(quotes) == 2


def test_parse_quotes_fields():
    soup = BeautifulSoup(SAMPLE_HTML, "html.parser")
    quotes = parse_quotes(soup)

    assert quotes[0]["author"] == "Albert Einstein"
    assert "change" in quotes[0]["tags"]
    assert "deep-thoughts" in quotes[0]["tags"]

    assert quotes[1]["author"] == "J.K. Rowling"
    assert quotes[1]["tags"] == "choices"


def test_parse_quotes_empty_page():
    soup = BeautifulSoup("<html><body></body></html>", "html.parser")
    quotes = parse_quotes(soup)
    assert quotes == []


if __name__ == "__main__":
    test_parse_quotes_extracts_all_quotes()
    test_parse_quotes_fields()
    test_parse_quotes_empty_page()
    print("All tests passed!")