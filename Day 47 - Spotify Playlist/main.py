import requests
import spotipy
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from datetime import date

def create_playlist(user_id, name):
    new_playlist = sp.user_playlist_create(user=user_id, name=name)
    return new_playlist["id"]

def add_music_to_playlist(playlist_id, title):
    # Search for Music
    search_results = sp.search(q=f"track:{title}", type='track', limit=1)
    items = search_results['tracks']['items']

    if not items:
        print(f"No tracks found for {title}")
        return
    
    track_uri = items[0]['uri']
    sp.playlist_add_items(playlist_id=playlist_id, items=track_uri)
    print(f"Added {title}")

load_dotenv()

statement = "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
required_date = input(statement)

if not required_date:
    required_date = date.today()

print(required_date)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

url = f"https://www.billboard.com/charts/hot-100/{required_date}/"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
list_songs = soup.select("div.o-chart-results-list-row-container")

titles = []

for song in list_songs:
    title = song.select_one("h3#title-of-a-story")
    singer = song.select_one("span.c-label  a")

    content_to_write = f"{title.text.strip()}"   
    try:
        with open("hot_100.txt", "a", encoding="utf-8") as file:
            file.write(content_to_write + "\n")
    except Exception as e:
        print(f"An error occured: {e}")
    
    titles.append(title.text.strip())

print("Data completely scraped...")


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Define the 'scope' (premission level)
scope = "user-library-read playlist-modify-public playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope=scope,
        open_browser=True,
        show_dialog=True
    )
)

print(sp.current_user()["id"])

# 2. Create the Playlist
USER_ID = sp.current_user()["id"]
PLAYLIST_NAME = f"Billboard Hot 100 – {required_date}"

playlist_id = create_playlist(USER_ID, PLAYLIST_NAME)

for title in titles:
    add_music_to_playlist(playlist_id, title)