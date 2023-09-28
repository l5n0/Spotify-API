import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import json

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
        artist_info = {
            "Artist Name": artist['name'],
            "Genres": artist['genres'],
            "Followers": artist['followers']['total'],
            "Popularity": artist['popularity']
        }

        top_tracks = sp.artist_top_tracks(artist['id'])
        track_info = [
            {"Track Number": i, "Track Name": track['name']} for i, track in enumerate(top_tracks['tracks'], start=1)
        ]

        artist_info["Top Tracks"] = track_info

        # Write to a JSON file
        with open(f"{artist_name}_info.json", "w", encoding='utf-8') as json_file:
            json.dump(artist_info, json_file, ensure_ascii=False, indent=4)

        print(f"Artist information for '{artist_name}' saved to {artist_name}_info.json")
    else:
        print(f"No artist found with the name '{artist_name}'")

if __name__ == '__main__':
    artist_name = input("Enter the name of the artist: ")
    get_artist_info(artist_name)
