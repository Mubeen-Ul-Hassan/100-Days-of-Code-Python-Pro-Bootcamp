import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}
url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.select("div.article-title-description")

for movie in movies:
    title = movie.select_one("h3.title")
    year_tag = movie.select_one("p strong")

    year = year_tag.get_text(strip=True) if year_tag else "N/A"

    content_to_write = f"{title.text.strip()} | {year}"
    try:
        with open("movies.txt", "a", encoding="utf-8") as file:
            file.write(content_to_write + "\n")
    except Exception as e:
        print(f"An error occured: {e}")
