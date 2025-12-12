import requests as r
import bs4 as bs
import pandas as pd

readingsite = r.get("https://www.scrapethissite.com/pages/forms/")
with open("ScrapTest.html", "w", encoding="utf-8") as f:
    f.write(readingsite.text)

with open("ScrapTest.html", "r", encoding="utf-8") as f:
    content = f.read()
    soup = bs.BeautifulSoup(content, "html.parser")

rows = soup.find_all("tr", class_="team")

team_names = []
years = []
wins = []
losses = []
ot_losses = []
win_percent = []

for row in rows:
    team_names.append(row.find("td", class_="name").text.strip())
    years.append(row.find("td", class_="year").text.strip())
    wins.append(row.find("td", class_="wins").text.strip())
    losses.append(row.find("td", class_="losses").text.strip())
    ot_losses.append(row.find("td", class_="ot-losses").text.strip())
    win_percent.append(row.find("td", class_="pct").text.strip())

teamInfo = {
    'team_names': team_names,
    'years': years,
    'wins': wins,
    'losses': losses,
    'ot_losses': ot_losses,
    'win_percent': win_percent
}

df = pd.DataFrame(teamInfo)
print(df)


