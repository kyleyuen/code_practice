class JukeBox:
	def __init__(self):
		self.songs = {}

	def add_song(self, song):
		self.songs[song.title] = song

	def play_song(self, song_title):
		self.songs[song_title].play()


class Song:
	def __init__(self, title, album, singer):
		self.title = title
		self.album = album
		self.singer = singer

	def play(self):
		pass