import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import os

SPOTIPY_CLIENT_ID = '285575c9b8fe4c4abbf3924cfcb46409'
SPOTIPY_CLIENT_SECRET = '7d122931137e4d7590b19bdd01f5f91d'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = "playlist-modify-private playlist-modify-public playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
))

def get_playlist_tracks(sp, playlist_id):
    tracks = []
    offset = 0
    while (results := sp.playlist_items(playlist_id, limit=50, offset=offset))['items']:
        tracks.extend([
            (
                item['track']['artists'][0]['name'],
                item['track']['album']['name'],
                item['track']['name'],
                item['track']['id']
            ) for item in results['items'] if item['track']
        ])
        offset += 50
    return tracks

def reorder_playlist(sp, playlist_id, tracks):
    track_ids = [track[3] for track in tracks]
    sp.playlist_replace_items(playlist_id, track_ids[:100])
    for i in range(100, len(track_ids), 100):
        sp.playlist_add_items(playlist_id, track_ids[i:i+100])

def save_to_file(filename, tracks, log_type):
    os.makedirs("spotify_backup", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        print(f"-------[ {log_type} ]--------")
        for i, (artist, album, song, track_id) in enumerate(tracks, 1):
            f.write(f"{i}. {artist},{album},{song},{track_id}\n")
            print(f"{i}. Artist: {artist}, Album: {album}, Song: {song}")

def backup_playlist(tracks, playlist_name):
    os.makedirs("spotify_backup", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"spotify_backup/backup_{playlist_name}_{timestamp}.txt"
    save_to_file(filename, tracks, "Backup")
    print(f"Backup: {filename}")
    return timestamp

playlist_id = '0LypOtuCZe9ugMOLDT8lrW'
playlist_name = sp.playlist(playlist_id)['name']

tracks = get_playlist_tracks(sp, playlist_id)
timestamp = backup_playlist(tracks, playlist_name)

sorted_tracks = sorted(set(tracks), key=lambda x: (x[0].lower(), x[1].lower(), x[2].lower()))
removed_tracks = [track for track in tracks if track not in sorted_tracks]

if removed_tracks:
    removed_file = f"spotify_backup/removed_{playlist_name}_{timestamp}.txt"
    save_to_file(removed_file, removed_tracks, "Removed")
    print(f"Removed: {removed_file}")
else:
    print("Không có bài hát nào bị xóa.")

reorder_playlist(sp, playlist_id, sorted_tracks)

print("Done.")
