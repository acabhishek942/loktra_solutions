#!/usr/bin/python

from __future__ import print_function
import sys, re

from bs4 import BeautifulSoup
import requests

def number_of_results(keyword):
	"""
	Get the number of results from webpage with given keyword.

	@param keyword: Keyword to appended in the URL
	@type keyword: string

	@var page: requests.models.Response object
	"""
	page = requests.get('http://www.shopping.com/products?KW='+keyword,
		allow_redirects=False)

	if page.status_code==302:
		print ("Resource temporarily unavailable. Fetching details from redirected URL")
		page = requests.get('http://www.shopping.com/products?KW='+keyword)
	soup = BeautifulSoup(page.content, "lxml")
	number_of_results = soup.find("span", attrs={'class': "numTotalResults"})

	if number_of_results is not None:
		numTotalResults=[]
		for i in str(number_of_results.text)[::-1]:
			if i==' ':
				break
			numTotalResults.append(i)
		print ("Total Number of Products : "+''.join(numTotalResults[::-1]))
	else:
		print ("No products for this keyword")
	

def all_results(keyword, page_number):
	"""
	Get all results from webpage with given keyword and page number.

	@param keyword: Keyword to appended in the URL.
	@type keyword: string

	@param page_number: Page number to be appended in the URL.
	@type page_number: string

	@var page: requests.models.Response object

	@var soup: bs4.Beautifulsoup object 

	@var all_results: bs4.Beautifulsoup object containing all results
	"""
	page=requests.get('http://www.shopping.com/products~PG-'+page_number+'?KW='+keyword,
		allow_redirects=False)

	if page.status_code==302:
		print ("Resource temporarily unavailable. Fetching details from redirected URL")
		page = requests.get('http://www.shopping.com/products~PG-'+page_number+'?KW='+keyword)

	soup = BeautifulSoup(page.content, "lxml")
	all_results=soup.find_all("div", id=re.compile('^quickLookItem-'))

	if len(all_results) != 0:

		for i in all_results:
			product_name=i.find("a", attrs={"class":"productName"})

			try:
				print (product_name['title'])
			except KeyError:

				product_name=product_name.find("span")['title']
				print (product_name)
	else:

		print ("Please check keyword/page number.")


if len(sys.argv)==2:
	number_of_results(str(sys.argv[1]))

elif len(sys.argv)==3:

	try: 
		int(sys.argv[2])	

	except ValueError:
		print ("Not a valid page number. Please try again")
		quit()

	all_results(str(sys.argv[1]), str(sys.argv[2]))
	

else:
	print ("Invalid number of arguments")
	print ("Please enter only keyword or keyword and page number")

