from bs4 import BeautifulSoup
import requests
import spotipy
# import lxml
import pandas
import numpy as np

import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select(selector="li h3", class_="c-title")
song_names = [song.getText().strip() for song in song_names_spans]


# ##########################################################################

Client_ID = "cc72a84d2e9742e2904adf11996ec457"
Client_secret = "0f624e51b34346f3a7a2399b75d41700"

ENDPOINT = "https://api.spotify.com/v1/users/{user_id}/playlists"
user_id = "smedjan"



scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=Client_ID,
    client_secret=Client_secret,
    cache_path="token.txt",
    show_dialog=True))

user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
# song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
