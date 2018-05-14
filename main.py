# Gas Calculator

# Imports
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def main():
	#capacity = input("What is the gas capacity of your car? ")
	site = 'https://www.gasbuddy.com/GasPrices/Washington/Seattle'
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(site, headers=hdr)
	page = urlopen(req)
	soup = BeautifulSoup(page)
	for td in soup.select('td'):
		print(td)


if __name__ == "__main__":
	main()