# Gas Calculator

# Imports
import requests
import json

def main():
	#capacity = input("What is the gas capacity of your car? ")
	api = 'http://devapi.mygasfeed.com/'
	api +=  '/stations/radius/49/150/10/reg/price/rfej9napna.json'
	my_response = requests.get(api)
	print(my_response.text)


if __name__ == "__main__":
	main()