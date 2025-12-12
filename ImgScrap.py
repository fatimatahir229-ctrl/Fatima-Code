import requests as r
import bs4 as bs
from tqdm import tqdm

baseUrl = "http://deckshop.pro/"

with open("C:\\Users\\LENOVO\\PyCharmMiscProject\\8\\card.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = bs.BeautifulSoup(content, "html.parser")

images = soup.find_all("img", class_="card")

for img in tqdm(images):
    src = img.get("src")
    full_url = baseUrl + src

    filename = full_url.split("/")[-1]

    # download the image
    img_data = r.get(full_url).content

    with open(filename, "wb") as outFile:
        outFile.write(img_data)