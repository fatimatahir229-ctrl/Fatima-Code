import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base = "https://www.w3schools.com/"
visited = set()

def scrape(url):
    if url in visited:
        return
    visited.add(url)

    print("Scanning:", url)

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    # Find and print button links
    for a in soup.find_all("a"):
        classes = a.get("class", [])
        if any(cls.startswith("w3-") or "btn" in cls.lower() for cls in classes):
            link = a.get("href")
            if link:
                print("   Button:", urljoin(base, link))

    # Follow all links on the page
    for a in soup.find_all("a"):
        href = a.get("href")
        if href and href.endswith(".asp"):
            next_url = urljoin(base, href)
            scrape(next_url)


scrape(base)
