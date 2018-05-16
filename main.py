# Gas Calculator

# Imports
import requests
import json

class PriceIn(Enum):
	CPG = 1
	CPL = 0

def measurement(choice):
	if choice == '1':
		return 1
	elif choice == '0':
		return 0
	else:
		return None

def main():
	price = input("What is the current price? (Enter in dollars, e.g. 3.88)")
	capacity = input("What is the gas capacity of your car? ")
	# TODO: Make own database because nobody has free car info api...
	choice = input("Enter 0 for Cents per Gallon, 1 for Cents per Litre: ")
	while (choice != '1' or choice != '0'):
		print("Invalid choice!")
		choice = input("Enter 0 for Cents per Gallon, 1 for Cents per Litre: ")
	# Enum 1 to mpg, 0 to litre
	price = conversion(PriceIn.measurement(choice))
	total_cost = price * capacity
	print('Total cost will be: ' + str(total_cost) + ' to fill up.')

if __name__ == "__main__":
	main()