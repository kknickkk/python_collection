#!/usr/bin/python3
from subprocess import call, check_output
import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import lxml
from lxml import etree
import re

def main():

	while True:
		choice = int(input('1. Manually enter song\n2. Search playlist\n'))
		
		if choice == 1:
			title = input('Enter song:\n')
			url = search(title + ' HQ')
			play(url)
		if choice == 2:
			query = input('Search playlist:\n')
			url = search(query + ' playlist')
			songlist = get_playlist(url)
			for song in songlist:
				play(song)

	return

def play(url):
	print('Playing:\n')
	get_title(url)
	string = 'youtube-dl -f140 -g ' + url 
	try:
		y = check_output(string.split())
		p = 'mpv ' + y.decode()
		call(p.split())
	except:
		pass

def search(title):

	query = urllib.parse.quote(title)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	    break
	return ('https://www.youtube.com' + vid['href'])


def get_title(url):
	youtube = etree.HTML(urllib.request.urlopen(url).read()) 
	video_title = youtube.xpath("//span[@id='eow-title']/@title") 
	print (''.join(video_title))

def get_playlist(url):
    sTUBE = ''
    cPL = ''
    amp = 0
    final_url = []
    
    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
            
    else:
        print('Incorrect Playlist.')
        exit(1)
    
    try:
        yTUBE = urllib.request.urlopen(url).read()
        sTUBE = str(yTUBE)
    except urllib.error.URLError as e:
        print(e.reason)
    
    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, sTUBE)
 
    if mat:
          
        for PL in mat:
            yPL = str(PL)
            if '&' in yPL:
                yPL_amp = yPL.index('&')
            final_url.append('http://www.youtube.com/' + yPL[:yPL_amp])
 
        all_url = list(set(final_url))
        return all_url
        
    else:
        print('No videos found.')
        exit(1)

if __name__ == '__main__':
	main()