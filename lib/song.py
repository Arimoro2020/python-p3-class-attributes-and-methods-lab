class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)


    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, self):
        if self.genre not in cls.genres:
            cls.genres.append(self.genre)
        else:
            pass

    @classmethod
    def add_to_artists(cls, self):
        if self.artist not in cls.artists:
            cls.artists.append(self.artist)
        else:
            pass


    @classmethod
    def add_to_genre_count(cls, self):
        if self.genre not in cls.genre_count:
            cls.genre_count[self.genre] = 1

        else:
            cls.genre_count[self.genre] += 1

    @classmethod
    def add_to_artist_count(cls, self):
        if self.artist not in cls.artist_count:
            cls.artist_count[self.artist] = 1

        else:
            cls.artist_count[self.artist] += 1


        

 

