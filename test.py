from bs4 import BeautifulSoup
import urllib.request, urllib.parse, re

def main():
	print('Getting staff urls...')

	staff_url = 'http://wa.amu.edu.pl/wa/en/staff_list'
	staff_content = get_content(staff_url)

	links = staff_content.find_all('a')

	urls = []
	for link in links:
		if len(link.get_text()) > 1:
			url = urllib.parse.urljoin('http://wa.amu.edu.pl', link['href'])
			urls.append(url)
			
	print('Staff urls found:')
	for url in urls:
		get_details(url)

def get_content(url):
		response = urllib.request.urlopen(url)
		data = response.read()
		doc = BeautifulSoup(data, 'html.parser')
		return doc.find(id='tresc_wlasciwa')

def get_details(url):
	try:
		content = get_content(url)
		links = content.find_all('a')
		header = content.find('h1')
		for link in links:
			if link.has_attr('href') and re.search('mailto:', link['href']):
				print(header.get_text(), link.get_text())
				break
	except:
		print('Error fetching from',url)

main()