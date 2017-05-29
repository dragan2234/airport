import string
from .seat import Seat

"""
Klasa koja reprezentuje avion.
Atrs:
	-model: model aviona
	-row_number: broj redova
	-seat_number: broj sedista
	-seats: recnik koji za svaki red sadrzi listu sedista(A,B...)
	-letter: pomocna promenljiva koja sadzi listu svih velikih slova. 
"""
class Plane(object):
	def __init__(self, model, row_number, seat_number):
		self.__model = model
		self.__row_number = row_number
		self.__seat_number = seat_number
		self.__seats = {}
		self.__letters = list(string.ascii_uppercase)
		self.make_seats()
	
	@property
	def model(self):
		return self.__model
	@property
	def row_number(self):
		return self.__row_number
	@property
	def seat_number(self):
		return self.__seat_number
	@property
	def seats(self):
		return self.__seats

	@model.setter
	def model(self, m):
		self.__model = m
	@row_number.setter
	def row_number(self, r):
		self.__row_number = r
	@seat_number.setter
	def seat_number(self, s):
		self.__seat_number = s
	@seats.setter
	def seats(self, s):
		self.__seats = s

	"""
	Funkcija koja na osnovu broja redova i broja sedista u redu pravi listu sedista.
	"""

	def make_seats(self):
		for r in range(1,self.__row_number + 1):
			for s in range(1,self.__seat_number + 1):
						#seat = Seat(r, self.__letters[s-1])		
						#self.__seats.append(seat)
						if not(r in self.__seats):
							self.__seats[r] = []
						self.__seats[r].append(self.__letters[s-1])
