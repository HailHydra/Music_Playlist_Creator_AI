def generate_song_artist_dict(playlist):
    """
    Takes the playlist (string from OpenAI) and returns a dictionary
    with song titles as keys and a dictionary of album, artist, and year as values.
    """
    # Split the response into a list of songs
    songs = playlist.strip().split("\n")

    # Create a dictionary to store song details
    song_artist_dict = {}

    # Loop through each song and extract details
    for song in songs:
        # Ensure the song follows the expected format: "Song - Album - Artist - Year"
        parts = song.split(" - ")
        if len(parts) == 4:  # Ensure the format is correct
            song_title, album, artist, year = [part.strip() for part in parts]
            song_artist_dict[song_title] = {
                "album": album,
                "artist": artist,
                "year": year,
            }

    return song_artist_dict