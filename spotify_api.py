import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
from tabulate import tabulate

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_id = client_id
client_secret = client_secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist_info(artist_name):
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    
    if results['artists']['total'] > 0:
        artist = results['artists']['items'][0]
        artist_info = [
            ["Artist Name:", artist['name']],
            ["Genres:", ', '.join(artist['genres'])],
            ["Followers:", artist['followers']['total']],
            ["Popularity:", artist['popularity']]
        ]

        top_tracks = sp.artist_top_tracks(artist['id'])
        track_info = [
            [f"{i}.", track['name']] for i, track in enumerate(top_tracks['tracks'], start=1)
        ]

        artist_table = tabulate(artist_info, tablefmt="html")
        top_tracks_table = tabulate(track_info, tablefmt="html")

        with open("artist_info.html", "w", encoding='utf-8') as html_file:
            html_file.write("<h1>Artist Information</h1>")
            html_file.write(artist_table)
            html_file.write("<h1>Top Tracks</h1>")
            html_file.write(top_tracks_table)

        print(f"Artist information for '{artist_name}' saved to artist_info.html")
    else:
        print(f"No artist found with the name '{artist_name}'")

if __name__ == '__main__':
    artist_name = input("Enter the name of the artist: ")
    get_artist_info(artist_name)
