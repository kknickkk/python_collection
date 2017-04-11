#!/usr/bin/python3
from subprocess import call, check_output
import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
from sys import exit
import lxml
from lxml import etree
import mpv


def main():

	while True:
		choice = int(input('1. Manually enter song\n2. Search playlist\n'))
		
		if choice == 1:
			title = input('Enter song:\n')
			url , title= search(title + ' HQ')
			play(url)
		if choice == 2:
			query = input('Search playlist:\n')
			url , title = search(query + ' playlist')
			songlist = get_playlist(url)
			for song in songlist:
				play(song)
				
	return

def play(url):
	print("Playing:\n")
	get_title(url)
	string = 'youtube-dl -f140 -g ' + url 
	i = ''
	try:
		y = check_output(string.split()).decode()
		player = mpv.MPV()
		player.play(y)
		i = input()
				
		if i == 'n':
			player.quit()
			del player
			return 

	except KeyboardInterrupt:
		exit()
	except:
		pass

def search(title):

	query = urllib.parse.quote(title)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")
	pop = soup.findAll(attrs={'class':'yt-uix-tile-link'}).pop(0)
	href = pop.get('href')
	title = pop.get('title')
	
	return ('https://www.youtube.com' + href), title

def get_title(url):
	youtube = etree.HTML(urllib.request.urlopen(url).read()) 
	video_title = youtube.xpath("//span[@id='eow-title']/@title") 
	print (''.join(video_title))


def get_playlist(url):
    final_url = []

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
            
    else:
        print('Incorrect Playlist.')
        exit(1)
    
    try:
        sTUBE = str(urllib.request.urlopen(url).read())
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