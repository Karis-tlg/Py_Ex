import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = '285575c9b8fe4c4abbf3924cfcb46409'
SPOTIPY_CLIENT_SECRET = '7d122931137e4d7590b19bdd01f5f91d'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = "playlist-modify-private playlist-modify-public playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

def get_playlist_tracks(sp, playlist_id, limit=50):
    tracks = []
    offset = 0
    while True:
        results = sp.playlist_items(playlist_id, limit=limit, offset=offset)
        items = results['items']
        if not items:
            break
        for item in items:
            track = item['track']
            if track:  
                artist = track['artists'][0]['name']
                album = track['album']['name']
                song = track['name']
                tracks.append((artist, album, song, track['id']))  
        offset += limit
    return tracks

def reorder_playlist(sp, playlist_id, tracks):
    track_ids = [track[3] for track in tracks]
    sp.playlist_replace_items(playlist_id, [])
    
    for i in range(0, len(track_ids), 100):  
        sp.playlist_add_items(playlist_id, track_ids[i:i+100])

playlist_id = '3cis3EjPrFL0Weis3TxkLW'  

tracks = get_playlist_tracks(sp, playlist_id)
sorted_tracks = sorted(list(set(tracks)), key=lambda x: (x[0].lower(), x[1].lower(), x[2].lower()))
reorder_playlist(sp, playlist_id, sorted_tracks)

print("Danh sách bài hát trong danh sách phát đã sắp xếp và loại bỏ trùng lặp:")
for artist, album, song, _ in sorted_tracks:
    print(f"Nghệ sĩ: {artist}, Album: {album}, Bài hát: {song}")


