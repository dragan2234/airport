import re
import prettytable
import string
from datetime import datetime, timedelta
from .plane import Plane
from .flight import Flight
from .user import User
from .ticket import Ticket


class Airport(object):

	def __init__(self):
		#{"broj leta": "let"}
		self.__flights = {}
		#{"model":"avion"}
		self.__planes = []
		#{"username":"password"}
		self.__users = {}
		self.fill()
		#lista slova iz koje se na osnovu pozicije izvlaci oznaka sedista
		self.__letters = list(string.ascii_uppercase)
		#heder za tabelu koja ispisuje letove
		self.__header = ["Fight No.","Src. Airport", "Dst. Airport","Start Date","End Date","Company","Days","Plane","Price"]

	def fill(self):
		p1 = Plane("Boing 747",14,7)
		p2 = Plane("Boing 737",13,6)
		p3 = Plane("Boing 727",12,5)
		p4 = Plane("Boing 717",11,4)
		self.__planes.append(p1)
		self.__planes.append(p2)
		self.__planes.append(p3)
		self.__planes.append(p4)

		f1 = Flight("B63029","WAW","VNO","1.3.2017. 11:14","1.3.2017. 15:15","AirSerbia",["Mon","Fri","Sat"],p3,230)
		f2 = Flight("FY2353","ATG","TUU","3.3.2017. 15:15","4.3.2017. 10:11","TurkishAirlines",["Tue","Fri","Sun"],p1,130)
		f3 = Flight("OU1925","QTT","FPO","4.3.2017. 10:11","4.3.2017. 23:00","TurkishAirlines",["Mon","Tue","Sat"],p2,250,)
		f4 = Flight("o", "WAW","TUU","4.3.2017. 23:00","5.3.2017. 13:00","AirSerbia",["Mon","Sun"],p4, 360)
		f5 = Flight("B63029","WAW","VNO","11.3.2017. 11:14","11.3.2017. 15:15","AirSerbia",["Mon","Fri","Sat"],p1,230)

		self.__flights[f1.id] = f1
		self.__flights[f2.id] = f2
		self.__flights[f3.id] = f3
		self.__flights[f4.id] = f4
		self.__flights[f5.id] = f5
		

		u1 = User("pera","123","Pera","Peric","seller")
		u2 = User("mara","123","Mara","Maric","seller")
		u3 = User("mica","123","Mica","Micic","manager")
		u4 = User("kica","123","Kica","Kicic","manager")
		self.__users[u1.username] = u1
		self.__users[u2.username] = u2
		self.__users[u3.username] = u3
		self.__users[u4.username] = u4

	@property
	def flights(self):
		return self.__flights
	@property
	def planes(self):
		return self.__planes
	@property
	def users(self):
		return self.__users
	@flights.setter
	def flights(self, flights):
		self.__flights = flights
	@planes.setter
	def planes(self, planes):
		self.__planes = planes
	@users.setter
	def users(self, users):
		self.__users = users

	def add_flight(self):
		pass

	"""
	Metoda koja vrsi kupovinu karte.
	Args:
		-time: vreme nakon koga se traze letovi. Ukoliko se ne unese, posmatra se trenutno vreme
		-source: aerodrom sa koga polece avion. Ukoliko se ne unese None
		-first_name: ime kupca
		-last_name: prezime kupca
		-nationality: nacionalnost kupca
		-passport: broj pasosa kupca
		-next_flight: identifikator za unos novog leta. Ako je true, po zavrsetku
					  dodavanja karte, dobice se opcija za unos nove
	"""
	def add_ticket(self, user, time = datetime.today(), company=None, first_name=None, last_name=None, nationality=None,passport=None, next_flight=True):
		print("*****ADD TICKET*****")
		x = prettytable.PrettyTable(["Flight No.", "Scr. Airport","Dst. Airport"])
		#lista dostupnih letova(letovi koji imaju slobodno mesto) i datum leta je > trenutnog
		available_flights = []
		#lista dostupnih brojeva letova
		flights_numbers = []
		print("*****Available flights*****")
		#iteracija kroz listu svih letova
		for f in list(self.__flights.values()):
			#ako je company None prikazi sve letove
			#ili ako f.company == company
			if (company is None or f.company == company):
				#ako ima slobodnih mesta i vreme poletanja je posle time
				if (len(f.seats) > 1 and f.start > time):
					#lista koja se koristi za prikaz
					available_flights.append([f.number, f.company, f.destination, f.start, f.end, f.company, f.days, f.plane, f.price])
					#lista slobonih letova(samo brojevi)
					flights_numbers.append(f.number)

		if (len(flights_numbers) == 0):
			print("There is no available flights.")
			return

		#prikazi letove
		self.display(available_flights)
		#unos broja leta
		flight_number = self.enter_flight_number(flights_numbers)
		#unos datuma leta
		flight_date = self.enter_flight_date(flight_number, time)
		#kljuc je broj leta + vreme poletanja
		flight_id = flight_date.strftime(flight_number+	"%d%m%Y%H%M")
		#konkretan let iz liste letova
		flight = self.__flights[flight_id]
		#prikaz slobodnih mesta
		self.display_seats(flight_id)
		#unos reda
		row = self.enter_row(flight)
		#unos sedista
		letter = self.enter_seat_letter(flight, row)
		#unos imena
		if (first_name is None):
			first_name = input("Enter passenger's first name:")
		#unos prezimena
		if(last_name is None):
			last_name = input("Enter passenger's last name:")
		#unos drzavljanstva
		if (nationality is None):
			nationality = input("Enter passenger's nationality:")
		#unos broja pasosa
		if (passport is None):
			passport = input("Enter passenger's passport number:")

		#kreiranje nove karte
		ticket = Ticket(first_name, last_name,nationality,passport, flight, row, letter, datetime.today(), flight.price, user)

		#dodaj kartu u listu karata za izabrani let
		self.__flights[flight_id].tickets.append(ticket)
		#izbaci sediste iz liste slobodnih sedista
		self.__flights[flight_id].seats[row].remove(letter)

		#ako zelimo unos novog leta, (bice false kada se poziva iz change_ticket motode)
		if (next_flight):
			#nova karta
			q = input("Do you want to buy another ticket? Enter 'no' for exit\n->")
			if (q != "no"):
				#vreme za novi let mora biti vece od vremena sletanja + 60 minuta
				tm = flight.end + timedelta(hours=1)
				#rekurzivno pozovi ponovno dodavanje sa novim vremenom i src, kao i korisnickim informacijama
				self.add_ticket(user, tm, flight.company, first_name, last_name, nationality, passport)

		print("---------Passanger informations---------")
		print(ticket)
		print("-----------Flight informations----------")
		print("Flight Number: %s\nSource Airport: %s\nDestination Airport: %s\n"%(flight.number,flight.source,flight.destination))
		print("----------")
		print("Seat Row: %d\nSeat Letter: %s\nPrice: %.2f\nDate: %s"%(row,letter,flight.price,flight.start))
		print("---------------------------")
		return
		
			

		"""
		Metoda koja omogucava izmenu karte.
		Args:
			-user: korisnik koji vrsi izmenu
		"""
	def change_ticket(self, user):
		flight_number = input("Enter Flight No:")
		
		#unos datuma dok se ne unese ispravan format
		while(True):
			try:
				d = input("Enter Date(dd.mm.yyyy. hh:mm):")
				flight_date = datetime.strptime(d, "%d.%m.%Y. %H:%M")
				break;
			except ValueError:
				print("Wrong date format!")
		
		#kljuc leta u listi 
		flight_id = flight_number + flight_date.strftime("%d%m%Y%H%M")
		#provera da li takav let posotji
		if (flight_id in self.__flights):
			flight = self.__flights[flight_id]
		else:
			print("Flight doesn't exists!")
			return

		passport = input("Enter passenger's passport number:")
		#iteriraj kroz karte
		for ticket in flight.tickets:
			#ako se brojevi pasosa pokalpaju
			if (ticket.passport_number == passport):
				#dodaj novu kartu
				self.add_ticket(user, first_name=ticket.first_name, last_name=ticket.last_name, nationality=ticket.nationality,passport=ticket.passport_number, next_flight=False)
				#obrisi staru kartu
				self.delete_ticket(user, flight_number, flight_date, passport)
		print("Successfully changed!")
		return
				


	"""
	Metoda koja vrsi brisanje karte. 
	Args:
		-user: prodavac koji brise kartu
		-flight_number: broj aviona za koji se brise karta
		-flight_date: datum leta za koji se brise karta
		-passport: broj pasosa putnika cija se karta brise

	"""
	def delete_ticket(self, user, flight_number = None, flight_date = None, passport = None):
		print("*****DELETE TICKET*****")
		if (flight_number is None):
			flight_number = input("Enter Flight No:")
		
		if (flight_date is None):
			#unos datuma dok se ne unese ispravan format
			while(True):
				try:
					d = input("Enter Date(dd.mm.yyyy. hh:mm):")
					flight_date = datetime.strptime(d, "%d.%m.%Y. %H:%M")
					break
				except ValueError:
					print("Wrong date format!")
		
		#kljuc leta u listi 
		flight_id = flight_number + flight_date.strftime("%d%m%Y%H%M")
		#provera da li takav let posotji
		if (flight_id in self.__flights):
			flight = self.__flights[flight_id]
		else:
			print("Flight doesn't exists!")
			return
		if (passport is None):
			while(True):
				option = input("Enter 1 for passport or 2 for seat:")
				if (int(option)>0 and int(option)<3):
						option = int(option)
						break
				else:
					print("Entry Type Error. Try again: -> ")
		else:
			#ako passport nije None, opcija je 1 da bi se pretrazivalo po broju pasosa
			option = 1

		#ako se brise po pasosu
		if (option == 1):
			if (passport is None):
				passport = input("Enter passenger's passport number:")
			for ticket in flight.tickets:
				if (ticket.passport_number == passport):
					#uklonu kartu iz liste
					flight.tickets.remove(ticket)
					#vrati zauzeto sediste
					flight.seats[ticket.seat_row].append(ticket.seat_letter)
					#sortiraj listu sedista
					flight.seats[ticket.seat_row].sort()
		#ako se brise po sedistu
		else:
			#unos broja reda
			while(True):
				row = input("Enter row:")
				if (option.isdigit()):
						break
				else:
					print("Entry Type Error. Try again: -> ")

			letter = input("Entter seat letter:").upper()
			for ticket in flight.tickets:
				if (ticket.seat_row == row and ticket.seat_letter == letter):
					#uklonu kartu iz liste
					flight.tickets.remove(ticket)
					#vrati zauzeto sediste
					flight.seats[ticket.seat_row].append(ticket.seat_letter)
					#sortiraj listu sedista
					flight.seats[ticket.seat_row].sort()

	def login(self):
		while(True):
			u = input("Username:")
			p = input("Password:")
			
			if (u in self.__users):
				if (self.__users[u].password == p):
					return u, self.__users[u].role
				else:
					print("+--------------+")
					print("|Wrong password|")
					print("+--------------+")
			else:
				print("+--------------------+")
				print("|User doesn't exists!|")
				print("+--------------------+")


	################################ DISPLAY ######################################
	def display_by_source(self,dep):
		x = []
		for f in list(self.__flights.values()):
			if (f.source == dep):
				x.append([f.number, f.source, f.destination, f.start, f.end, f.company, f.days, f.plane, f.price])
		self.display(x)
	def display_by_destination(self,dest):
		x = []
		for f in list(self.__flights.values()):
			if (f.destination == dest):
				x.append([f.number, f.source, f.destination, f.start, f.end, f.company, f.days, f.plane, f.price])
		self.display(x)

	def display_by_start_date(self,date):
		x = []
		date = datetime.strptime(date,"%d.%m.%Y.")
		for f in list(self.__flights.values()):
			d = f.start#datetime.strptime(f.start, '%d.%m.%Y. %H:%M')
			if (d.year == date.year and d.month == date.month and d.day == date.day):
				x.append([f.number, f.source, f.destination, f.start, f.end, f.company, f.days, f.plane, f.price])
		self.display(x)

	def display_by_end_date(self,date):
		x = []
		date = datetime.strptime(date,"%d.%m.%Y.")
		for f in list(self.__flights.values()):
			d = f.end#datetime.strptime(f.end, '%d.%m.%Y. %H:%M')
			if (d.year == date.year and d.month == date.month and d.day == date.day):
				x.append([f.number, f.source, f.destination, f.start, f.end, f.company, f.days, f.plane, f.price])
		self.display(x)
	def display_by_start_time(self,time):
		x = []
		date = datetime.strptime(time,"%H:%M")
		for f in list(self.__flights.values()):
			d = f.start#datetime.strptime(f.start, '%d.%m.%Y. %H:%M')
			if (d.hour == date.hour and d.minute == date.minute):
				x.append([f.number, f.source, f.destination, f.start, f.end, f.company, f.days, f.plane, f.price])
		self.display(x)
	def display_by_end_time(self,time):
		x = []
		date = datetime.strptime(time,"%H:%M")
		for f in list(self.__flights.values()):
			d = f.end#datetime.strptime(f.end, '%d.%m.%Y. %H:%M')
			if (d.hour == date.hour and d.minute == date.minute):
				x.append([f.number, f.source, f.destination, f.start, f.end, f.company, f.days, f.plane, f.price])
		self.display(x)

	def display_by_company(self,company):
		x = []
		for f in list(self.__flights.values()):
			if (f.company == company):
				x.append([f.number, f.source, f.destination, f.start, f.end, f.company, f.days, f.plane, f.price])
		self.display(x)


	def display(self, rows):
		x = prettytable.PrettyTable(self.__header)
		for r in rows:
			x.add_row(r)
		print(x)

	"""
	Metoda koja prikazuje slobodna sedista za izabrani let.
	Args:
		-flight_number: broj leta za koji se prikazuju slobodna sedista
	"""
	def display_seats(self, flight_id):
		x = prettytable.PrettyTable(["Row","Seats"])
		seats = self.__flights[flight_id].seats
		for r in seats:
			x.add_row([r, ','.join(seats[r])])
		print(x)
	###################################### END DISPLAY ############################

	"""
	Dijalog za unos broja reda.
	Args:
		-flight: let 
	"""
	def enter_row(self, flight):
		while(True):
			s = input("Enter row:")
			if (s.isdigit()):
				if (int(s) in flight.seats):
					return int(s)
				else:
					print("Row doesn't exist!")
			else:
				print("Entry Type Error. Try again: -> ")

	"""
	Dijalog za unos broja leta.
	Args:
		-flights_number: lista mogucih letova
	"""
	def enter_flight_number(self, flights_numbers):
		while(True):
			x = input("Flight number:")	
			if (x in flights_numbers):
				return x
			else:
				print("Flight doesn't exist!")

	"""
	Dijalog za unos oznake sedista.
	Args:
		-flight: let
		-row: red u kom se nalazi sediste
	"""
	def enter_seat_letter(self, flight, row):
		while(True):
			s = input("Enter seat letter:")
			if (s in flight.seats[row]):
				return s
			else:
				print("Seat doesn't exist!")

	"""
	Dijalog za unos datuma leta.
	Args:
		-flight_number: broj leta
		-time: donja granica leta
	"""
	def enter_flight_date(self, flight_number, time):
		available_flights = []
		for f in list(self.__flights.values()):
			if (f.number == flight_number and f.start >= time):
				available_flights.append(f)

		if (len(available_flights) > 0):
			print("+----------------------+")
			print("|        Date          |")
			print("+----------------------+")
			i = 1
			for f in available_flights:
				print("| (%d) %s |"%(i, f.start.strftime("%d.%m.%Y. %H:%M")))
				i += 1
			print("+----------------------+")

			while(True):
				s = input("Enter row number:")
				if (s.isdigit() and int(s)>0 and int(s) <= len(available_flights)):
					return available_flights[int(s)-1].start
			else:
				print("Entry Error. Try again: -> ")

	"""
	Metoda koja prikazuje karte.
	Args:
		-selling_day: dan prodaje karte
		-start_date: datum poletanja aviona
		-seller: prodavac
	"""
	def get_tickets(self, selling_day = None, start_date = None, seller = None):
		#kreiraj tabelu
		x = prettytable.PrettyTable(["First Name","Last Name","Nationality","Passport","Flight No","Row Number","Seat","Customer","Selling Day"])
		#ako je kriterijum pretrage dan prodaje
		if (selling_day is not None):
			#konvertuj string u datum
			selling_day = datetime.strptime(selling_day, "%d.%m.%Y.")
			#iteriraj kroz sve letove
			for flight in list(self.__flights.values()):
				#iteriraj kroz sve karte 
				for ticket in flight.tickets:
					#ako se datumi prodaje poklapaju dodaj ga u tabelu
					if (self.compare_dates(ticket.selling_day, selling_day)):
						x.add_row([ticket.first_name, ticket.last_name, ticket.nationality, ticket.passport_number, ticket.flight.number, ticket.seat_row, ticket.seat_letter, ticket.customer, ticket.selling_day])

		#ako je kriterijum pretrage dan poletanja
		if (start_date is not None and seller is None):
			#konvertuj string u datum
			start_date = datetime.strptime(start_date, "%d.%m.%Y.")
			#iteriraj kroz sve letove
			for flight in list(self.__flights.values()):
				#iteriraj kroz sve karte
				for ticket in flight.tickets:
					#ako se datumi poletanja poklapaju dodaj u tabelu
					if (self.compare_dates(ticket.flight.start, start_date)):
						x.add_row([ticket.first_name, ticket.last_name, ticket.nationality, ticket.passport_number, ticket.flight.number, ticket.seat_row, ticket.seat_letter,ticket.customer, ticket.selling_day])

		#ako je kriterijum pretrage dan poletanja i prodavac
		if (start_date is not None and seller is not None):
			#konvertuj string u datum
			start_date = datetime.strptime(start_date, "%d.%m.%Y.")
			#iteriraj kroz sve letove
			for flight in list(self.__flights.values()):
				#iteririaj kroz sve karte
				for ticket in flight.tickets:
					#ako se datumi poklapaju
					if (self.compare_dates(ticket.flight.start, start_date)):
						#ako se prodavac poklapa dodaj u tabelu
						if (ticket.customer == seller):
							x.add_row([ticket.first_name, ticket.last_name, ticket.nationality, ticket.passport_number, ticket.flight.number, ticket.seat_row, ticket.seat_letter,ticket.customer, ticket.selling_day])
		#prikazi tabelu							
		print(x)
		
	"""
	Metoda koja prikazuje izvestaj o prodaji karata.
	Args:
		-selling_day: dan prodaje karte
		-start_date: datum poletanja aviona
		-seller: prodavac
	"""
	def get_statistic(self, selling_day = None, start_date = None, seller = None):
		count = 0
		price = 0

		#ako je kriterijum pretrage dan prodaje
		if (selling_day is not None):
			#konvertuj string u datum
			selling_day = datetime.strptime(selling_day, "%d.%m.%Y.")
			#iteriraj kroz sve letove
			for flight in list(self.__flights.values()):
				#iteriraj kroz sve karte 
				for ticket in flight.tickets:
					#ako se datumi prodaje poklapaju povecaj sume
					if (self.compare_dates(ticket.selling_day, selling_day)):
						count += 1
						price += ticket.price

		#ako je kriterijum pretrage dan poletanja
		if (start_date is not None and seller is None):
			#konvertuj string u datum
			start_date = datetime.strptime(start_date, "%d.%m.%Y.")
			#iteriraj kroz sve letove
			for flight in list(self.__flights.values()):
				#iteriraj kroz sve karte
				for ticket in flight.tickets:
					#ako se datumi poletanja poklapaju povecaj sume
					if (self.compare_dates(ticket.flight.start, start_date)):
						count += 1
						price += ticket.price

		#ako je kriterijum pretrage dan poletanja i prodavac
		if (start_date is not None and seller is not None):
			#konvertuj string u datum
			start_date = datetime.strptime(start_date, "%d.%m.%Y.")
			#iteriraj kroz sve letove
			for flight in list(self.__flights.values()):
				#iteririaj kroz sve karte
				for ticket in flight.tickets:
					#ako se datumi poklapaju
					if (self.compare_dates(ticket.flight.start, start_date)):
						#ako se prodavac poklapa povecaj sume
						if (ticket.customer == seller):
							count += 1
							price += ticket.price
		print("Number of sold tickets: %d\nMoney earned: %.2f"%(count, price))

	"""
	Metoda koja vraca ukupan broj i cenu prodatih karata u poslednjih 30 dana, po prodavcima.
	"""
	def statistic30(self):
		#30 dana u nazad od danasnjeg dana
		d = datetime.today()-timedelta(days=30)
		#recnik oblika "username":[broj prodatih, cena]
		sellers = {}
		#iteriraj kroz letove
		for flight in list(self.__flights.values()):
			#iteriraj kroz karte
			for ticket in flight.tickets:
				#ako u recniku ne postoji kupac, dodaj ga
				if (ticket.customer not in sellers):
					sellers[ticket.customer] = [0,0]
				#ako se datumi poklapaju
				if (ticket.selling_day > d):
					#povecaj broj prodatih karata
					sellers[ticket.customer][0] += 1
					#povecaj cenu
					sellers[ticket.customer][1] += ticket.price

		#iteriraj kroz recnik i ispisi
		for seller in sellers:
			print("Customer: %s"%(seller))
			print("Total tickets: %s"%(sellers[seller][0]))
			print("Total money earned: %.2f"%(sellers[seller][1]))
	"""
	Metoda koja poredi dva datuma. Bez vremena.
	"""
	def compare_dates(self, d1, d2):
		if (d1.day == d2.day and d1.month == d2.month and d1.year == d2.year):
			return True
		return False