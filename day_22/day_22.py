import json

import requests
from bs4 import BeautifulSoup

html_code = """
<!DOCTYPE html>
<html>
    <head><title>AI Tech Hub</title></head>
    <body>
        <h1 class="main-title">Welcome to Python AI</h1>
        <p class="description">We build autonomous neural networks and agents.</p>
        <p class="author">Instructor: DeepMind Team</p>
        <a href="https://python.org">Official Python Site</a>
    </body>
</html>
"""

soup = BeautifulSoup(html_code, "html.parser")

print("Title tag:       ", soup.title.text)
print("Main Paragraph:      ", soup.find("h1").text)
print("Paragraph 1:         ", soup.find("p").text)

link = soup.find("a")
print("Link Text:       ", link.text)
print("Actual Web Link:        ", link["href"])


all_paragraphs = soup.find_all("p")

print(f"\nFound {len(all_paragraphs)} paragraphs: ")
for p in all_paragraphs:
    print(" -", p.text)

author_tag = soup.find("p", class_="author")
print("Targeted Author Tag:", author_tag.text)

url = "http://quotes.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    live_soup = BeautifulSoup(response.text, "html.parser")
    quotes = live_soup.find_all("div", class_="quote")
    print(f"Total quotes found on page: {len(quotes)}\n")
    scraped_quotes = []
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tag_elements = q.find_all("a", class_="tag")
        tags = [t.text for t in tag_elements]

        scraped_quotes.append({"quote": text, "author": author, "tags": tags})
        print(f"{text}")
        print(f"  - by {author}\n")

    with open("day_22/quotes.json", "w", encoding="utf-8") as f:
        json.dump(scraped_quotes, f, indent=4)
    print(f"Successfully saved {len(scraped_quotes)} quotes to quotes.json")

else:
    print(f"Failed to fetch webpage: Status {response.status_code}")
