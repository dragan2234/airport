"""
Klasa koja reprezentuje korisnika.
Atrs:
	-username: korisnicko ime
	-password: lozinka
	-first_name: ime
	-last_name: prezime
	-role: uloga
"""
class User(object):
	def __init__(self, username, password, first_name, last_name, role):
		self.__username = username
		self.__password = password
		self.__first_name = first_name
		self.__last_name = last_name
		self.__role = role

	@property
	def username(self):
		return self.__username

	@username.setter
	def username(self, u):
		self.__username = u

	@property
	def password(self):
		return self.__password

	@password.setter
	def password(self, p):
		self.__password = p

	@property
	def first_name(self):
		return self.__first_name

	@first_name.setter
	def first_name(self, f):
		self.__first_name = f

	@property
	def last_name(self):
		return self.__last_name

	@last_name.setter
	def last_name(self, l):
		self.__first_name = l

	@property 
	def role(self):
		return self.__role

	@role.setter
	def role(self, r):
		self.__role = r
