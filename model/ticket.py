"""
Klasa koja reprezentuje kartu.
Attrs:
	-fist_name: ime kupca
	-last_name: prezime kupca
	-nationality: drzavljanstvo
	-passport_nubmer: broj pasosa
	-fligh: objekat tj. konkretan let kom karta pripada
	-seat_letter: oznaka sedista
	-seat_row: broj reda
	-selling_day: vreme prodaje karte
	-price: cena karte
	-customer: prodavac koji je prodao kartu
"""

class Ticket(object):
	def __init__(self, first_name, last_name, nationality, passport_number, flight, seat_row, seat_letter, selling_day, price, customer):
		self.__first_name = first_name
		self.__last__name = last_name
		self.__nationality = nationality
		self.__passport_number = passport_number
		self.__flight = flight
		self.__seat_letter = seat_letter
		self.__seat_row = seat_row
		self.__selling_day = selling_day
		self.__price = price
		self.__customer = customer

	@property
	def first_name(self):
		return self.__first_name
	@property
	def last_name(self):
		return self.__last__name
	@property
	def nationality(self):
		return self.__nationality
	@property
	def passport_number(self):
		return self.__passport_number
	@property
	def flight(self):
		return self.__flight
	@property
	def seat_row(self):
		return self.__seat_row
	@property
	def seat_letter(self):
		return self.__seat_letter
	@property
	def selling_day(self):
		return self.__selling_day
	@property
	def price(self):
		return self.__price
	@property
	def customer(self):
		return self.__customer

	@first_name.setter
	def first_name(self, first_name):
		self.__first_name = first_name
	@last_name.setter
	def last_name(self, last_name):
		self.__last__name = last_name
	@nationality.setter
	def nationality(self, nationality):
		self.__nationality = nationality
	@passport_number.setter
	def passport_number(self, passport_number):
		self.__passport_number = passport_number
	@flight.setter
	def flight(self, f):
		self.__flight = f
	@seat_row.setter
	def seat_row(self, s):
		self.seat_row = s
	@seat_letter.setter
	def seat_letter(self, s):
		self.__seat_letter = s
	@selling_day.setter
	def selling_day(self, s):
		self.__selling_day = s
	@price.setter
	def price(self, p):
		self.__price = p
	@customer.setter
	def customer(self, c):
		self.__customer = c
		
	def __str__(self):
		return "First Name: %s\nLast Name: %s\nNationality: %s\nPassport: %s\n"%(self.__first_name, self.__last__name, self.__nationality, self.__passport_number)
