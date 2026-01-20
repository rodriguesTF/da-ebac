import requests
from bs4 import BeautifulSoup
import csv

url = "https://github.com/trending"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

url = "https://github.com/trending"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

repositorios = soup.find_all("article", class_="Box-row")[:10]

dados = []

for idx, repo in enumerate(repositorios, start=1):
    # ranking
    ranking = idx

    # project
    project = repo.h2.a.get_text(strip=True).replace(" ", "")

    # language
    lang_tag = repo.find("span", itemprop="programmingLanguage")
    language = lang_tag.get_text(strip=True).lower() if lang_tag else ""

    # stars (total)
    stars_tag = repo.find("a", href=lambda x: x and "stargazers" in x)
    stars = stars_tag.get_text(strip=True).replace(",", "") if stars_tag else "0"

    # forks
    forks_tag = repo.find("a", href=lambda x: x and "forks" in x)
    forks = forks_tag.get_text(strip=True).replace(",", "") if forks_tag else "0"

    # stars today
    stars_today_tag = repo.find("span", class_="d-inline-block float-sm-right")
    stars_today = stars_today_tag.get_text(strip=True).split()[0].replace(",", "") if stars_today_tag else "0"

    dados.append([
        ranking,
        project,
        language,
        stars,
        stars_today,
        forks
    ])

dados