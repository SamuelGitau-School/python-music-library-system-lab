class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name: str, artist: str, genre: str):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments total song count by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre: str):
        """Adds new genre to class attribute genres (unique values only)."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist: str):
        """Adds new artist to class attribute artists (unique values only)."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre: str):
        """Increments genre count or sets initial count to 1."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist: str):
        """Increments artist count or sets initial count to 1."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
