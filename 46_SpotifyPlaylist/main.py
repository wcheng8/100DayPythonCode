import os

import requests
import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv('../.env')

pp = pprint.PrettyPrinter(indent=4)
SPOTIPY_CLIENT_ID=os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET=os.getenv('SPOTIPY_CLIENT_SECRET')

date = input("What date would you like the playlist of? (MM-YYYY)? ")
date_month = date.split("-")[0]
date_year = date.split("-")[1]

URL = f'https://www.billboard.com/charts/hot-100/{date_year}-{date_month}-12/'
# URL = f'https://www.billboard.com/charts/hot-100/2000-03-12/'
# year = 2000
request = requests.get(URL)
song_soup = BeautifulSoup(request.text,'html.parser')
title_list = song_soup.select("main div li h3")
new_title_list = [title.get_text()[1:] for title in title_list]
print((new_title_list))

# Spotipy Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path='token.txt'
    )
)

# Find current user
user = sp.current_user()['id']
print(user)

# Searching songs
song_uris = []
for song in new_title_list:
    song = song[:len(song)-1]
    result = sp.search(q=f'track:{song} year:{date_year}')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist and has been skipped")

song_total = len(song_uris)

# Creating a private playlist on spotify
playlist = sp.user_playlist_create(user=user, name=f'{date_year} Billboard 100', public=False)
pp.pprint(playlist)

# Add songs to new playlist
sp.playlist_add_items(playlist_id=playlist['id'],items=song_uris)

print(f'A total of {song_total} was added to your playlist and {100-song_total} songs were skipped')

