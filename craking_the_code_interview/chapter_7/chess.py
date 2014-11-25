class Board:
	def __init__(self):
		pass



class Piece:
	def __init__(self, piece_type, position):
		self.piece_type = piece_type
		self.position = position



class Chess:
	def __init__(self):
		self.board = Board()
