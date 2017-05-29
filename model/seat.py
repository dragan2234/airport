"""
Klasa koja predstavlja sediste.
Attrs:
	-row: broj sedista
	-letter: oznaka sedista u redu
"""
class Seat(object):
	def __init__(self, row, letter):
		self.__row = row
		self.__letter = letter

	@property
	def row(self):
		return self.__row
	@property
	def letter(self):
		return self.__letter

	@row.setter
	def row(self, r):
		self.__row = r
	@letter.setter
	def letter(self, l):
		self.__letter = l