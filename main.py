import json

def load(json_data):
    # Load the JSON data
    data = json.loads(json_data)

    # Retrieve the desired fields
    playlist_title = data['playlistTitle']
    playlist_author = data['playlistAuthor']
    sync_url = data['customData']['syncURL']

    # Retrieve songs details
    songs = data['songs']
    songlist = []
    for song in songs:
        songlist.append(song)
    
    return playlist_title, playlist_author, sync_url, songlist