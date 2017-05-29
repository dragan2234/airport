from datetime import datetime
import string

"""
Klasa koja reprezentuje jedan avionski let.
Attrs:
	-id: id leta- broj leta + vreme poletanja
	-nubmer: broj leta
	-souce: odrediste
	-destination: destinacija
	-start: vreme poletanja
	-end: vreme sletanja
	-company: prevoznik
	-days: dani kojima saobraca(lista)
	-plane: model aviona
	-price: cena leta
	-seats: sedista; recnik koji za svaki red ima listu sedista 
			npr. {'1':["A","B","C"]}
	-tickets: lista prodatih karata
"""
class Flight(object):
	def __init__(self):
		self.__id = None
		self.__number = None
		self.__source = None
		self.__destination = None
		self.__start = None
		self.__end = None
		self.__company = None
		self.__days = []
		self.__plane = None
		self.__price = None
		self.__seats = {}
		self.__tickets = []
	"""
	Konstruktor:
	Args:
		-start: datum(string)
		-plane: objekat tj. konkretan avion
	"""
	def __init__(self, number, source, destination, start, end, company, days, plane, price):
		self.__number = number
		self.__source = source
		self.__destination = destination
		self.__start =  datetime.strptime(start, '%d.%m.%Y. %H:%M')
		self.__end =  datetime.strptime(end, '%d.%m.%Y. %H:%M')
		self.__company = company
		self.__days = days
		self.__plane = plane.model
		self.__price = price
		self.__seats = plane.seats
		self.__tickets = []
		self.__id = number + self.__start.strftime("%d%m%Y%H%M")

	@property
	def id(self):
		return self.__id
	@property
	def number(self):
		return self.__number
	@property
	def source(self):
		return self.__source
	@property
	def destination(self):
		return self.__destination
	@property
	def start(self):
		return self.__start
	@property
	def end(self):
		return self.__end
	@property
	def company(self):
		return self.__company
	@property
	def days(self):
		return self.__days
	@property
	def plane(self):
		return self.__plane
	@property
	def price(self):
		return self.__price
	@property
	def seats(self):
		return self.__seats
	@property
	def tickets(self):
		return self.__tickets

	@id.setter
	def id(self, i):
		self.__id = i
	@number.setter
	def number(self, n):
		self.__number = n
	@source.setter
	def source(self, d):
		self.__source = d
	@destination.setter
	def destination(self, d):
		self.__destination = d
	@start.setter
	def start(self, s):
		self.__start = s
	@end.setter
	def end(self, f):
		self.__end = f
	@company.setter
	def company(self, c):
		self.__company = c
	@days.setter
	def days(self, d):
		self.__days = d
	@plane.setter
	def plane(self, p):
		self.__plane = p
	@price.setter
	def price(self, p):
		self.__price = p
	@seats.setter
	def seats(self, s):
		self.__seats = s

	"""
	Metoda koja dodaje kartu u listu karata.
	Args:
		-ticket: objekat tj. konkretna karta
	"""
	def add_ticket(self, ticket):
		self.__tickets.append(ticket)

