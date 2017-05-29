from model.user import User
from model.airport import Airport
from datetime import datetime

def option():
    while(True):
        s = input("Enter a number: ")
        if (s.isdigit()):
            return int(s)
        else:
            print("Entry Type Error. Try again: -> ")
    

def menu_seller():
	print("\n   ____________________________")
	print("1.  Search by source")
	print("2.  Search by destination")
	print("3.  Search by start date")
	print("4.  Search by end date ")
	print("5.  Search by start time")
	print("6.  Search by end time")
	print("7.  Search by company")
	print("8.  Sell ticket")
	print("9.  Change ticket")
	print("10. Delete ticket")
	print("11. Log out")
	print("   ---------------------------")

	while (True):
		x = option()
		if (x>=1 and x<=12 ):
			return x

def menu_manager():
	print("\n    ____________________________")
	print("1.  Search by source")
	print("2.  Search by destination")
	print("3.  Search by start date")
	print("4.  Search by end date ")
	print("5.  Search by start time")
	print("6.  Search by end time")
	print("7.  Search by company")
	print("8.  Sold tickets for day")
	print("9.  Sold tickets for flight day")
	print("10. Sold tickets for flight day and seller")
	print("11. Statistic for day")
	print("12. Statistic for flight day")
	print("13. Statistic for flight day and seller")
	print("14. Statistic for sellers in past 30 days")
	print("15. Log out")
	print("    ---------------------------")

	while (True):
		x = option()
		if (x>=1 and x<= 16):
			return x


def enter_date():
	#unos datuma dok se ne unese ispravan format
	while(True):
		try:
			d = input("Enter Date(dd.mm.yyyy.):")
			flight_date = datetime.strptime(d, "%d.%m.%Y.")
			break
		except ValueError:
			print("Wrong date format!")
	#vrati string
	return flight_date.strftime("%d.%m.%Y.")
def enter_time():
	#unos datuma dok se ne unese ispravan format
	while(True):
		try:
			d = input("Enter Time(hh:mm):")
			flight_date = datetime.strptime(d, "%H:%M")
			break
		except ValueError:
			print("Wrong time format!")
	#vrati string
	return flight_date.strftime("%H:%M")
def main():
	a = Airport()
	user, role = a.login()

	while(True):
		if (role == "seller"):
			ans = menu_seller()
			while(ans != 12):
				if (ans == 1):
					src = input("Enter source:")
					a.display_by_source(src)
				elif(ans == 2):
					dst = input("Enter destination:")
					a.display_by_destination(dst)
				elif(ans == 3):
					start = enter_date()
					a.display_by_start_date(start)
				elif(ans == 4):
					end = enter_date()
					a.display_by_end_date(end)
				elif(ans == 5):
					start = enter_time()
					a.display_by_start_time(start)
				elif(ans == 6):
					end = enter_time()
					a.display_by_end_time(end)
				elif(ans == 7):
					company = input("Enter company:")
					a.display_by_company(company)
				elif(ans == 8):
					a.add_ticket(user)
				elif(ans == 9):
					a.change_ticket(user)
				elif(ans == 10):
					a.delete_ticket(user)
				elif(ans == 11):
					user, role = a.login()
					break

				ans = menu_seller()
		else:
			ans = menu_manager()
			while( ans != 16):
				if (ans == 1):
					src = input("Enter source:")
					a.display_by_source(src)
				elif(ans == 2):
					dst = input("Enter destination:")
					a.display_by_destination(dst)
				elif(ans == 3):
					start = enter_date()
					a.display_by_start_date(start)
				elif(ans == 4):
					end = enter_date()
					a.display_by_end_date(end)
				elif(ans == 5):
					start = enter_time()
					a.display_by_start_time(start)
				elif(ans == 6):
					end = enter_time()
					a.display_by_end_time(end)
				elif(ans == 7):
					company = input("Enter company:")
					a.display_by_company(company)
				elif(ans == 8):
					day = enter_date()
					a.get_tickets(selling_day = day)
				elif(ans == 9):
					day = enter_date()
					a.get_tickets(start_date = day)
				elif(ans == 10):
					seller = input("Enter seller:")
					day = enter_date()
					a.get_tickets(start_date = day, seller = seller)
				elif(ans == 11):
					day = enter_date()
					a.get_statistic(selling_day = day)
				elif(ans == 12):
					day = enter_date()
					a.get_statistic(start_date = day)
				elif(ans == 13):
					seller = input("Enter seller:")
					day = enter_date()
					a.get_statistic(start_date = day, seller = seller)
				elif(ans == 14):
					a.statistic30()
				elif(ans == 15):
					user, role = a.login()
					break
				ans = menu_manager()

if __name__ == '__main__':
	main()