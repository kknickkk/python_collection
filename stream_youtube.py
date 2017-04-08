from subprocess import call, check_output
import urllib
import urllib2
from sys import argv
from bs4 import BeautifulSoup

def main():

	#title = argv[1]
	while True:
		title = str(raw_input('Enter song:\n'))
		url = search(title + ' HQ')
		play(url)
	
	return

def play(url):

	string = 'youtube-dl -f140 -g ' + url 
	y = check_output(string.split())
	p = 'mpv ' + y
	call(p.split())

def search(title):

	query = urllib.quote(title)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	    break
	return ('https://www.youtube.com' + vid['href'])


if __name__ == '__main__':
	main()