#! /usr/local/bin/python
from subprocess import call, check_output
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
from glob import glob
from colorama import Fore, Back, Style

path = '/Users/Nick/Desktop/Python/'
output_folder = 'Downloaded'

def main():
	print_red('Due to ffmpeg restrictions songs will be downloaded in a subfolder: ' + output_folder)

	if len(sys.argv) == 2:
		try:
 			f = open(sys.argv[1], 'r')
 		except IndexError:
 			print "Can't open file, try again.\nUsage: youtube_download.py <text file w/ songs>\n"
 			return
 		songlist = f.read()
		songlist = songlist.split('\n')
	else:
		songlist = user_interactive()
	
	check_folder()
	n = len(songlist)
	i = 0
	while i < n:
		if songlist[i] == '':
			break
		print_red("Downloading: " + songlist[i])
		url = get_song_url(songlist[i] + ' HQ ')
		print url
		out = download_song(url)
		filename = get_filename(out)
		add_metadata(songlist[i], filename)
		i += 1


def user_interactive():
	songs = raw_input('Enter songs to download in the format:\nTitle - Artist || Title - Artist || ...\n')
	songs = songs.split('||')
	return songs

def check_folder():
	folders = glob(path + '*')
	if path + output_folder not in folders:
		call(['mkdir', path + output_folder])

def get_filename(out):
	index = out.find('[ffmpeg] Destination:')
	s = out[index :]
	s = s.split('\n')
	s = s[0]
	s = s.strip('[ffmpeg] Destination:')
	#print_green(s)
	return s


def add_metadata(data, filename):
	
	data_s = data.split(' - ')
	artist = data_s[1].title()
	title = data_s[0].title()
	files = glob(path + '*.mp3')
	
	filename = filename.strip(path)
	image = filename.strip('.mp3') + '.jpg'
	newfile = filename.strip('.mp3') + '_NEW.mp3'
	
	command = 'ffmpeg$-i$' + filename + '$-i$' + image + '$-c$copy$-map$0$-map$1$-metadata:s:v$title="Album cover"$-metadata:s:v$comment="Cover (Front)"$-metadata$title=' + title + "$-metadata$artist=" + artist + '$' + newfile
	call(command.split('$'))
	call(['rm', path + filename])
	call(['rm', path + image])
	call(['mv', path + newfile, path + output_folder + '/' + title + ' - ' + artist + '.mp3'])

def download_song(url):

	command = 'youtube-dl --extract-audio --write-thumbnail --audio-format mp3 --audio-quality 0 -o ' + path + '%(title)s.%(ext)s ' + url 
	out = check_output(command.split())
	return out.decode()

def get_song_url(textToSearch):

	query = urllib.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	    break

	return ('https://www.youtube.com' + vid['href'])


def print_red(text):
        print(Fore.RED + Style.BRIGHT+ str(text) + Style.RESET_ALL )
        return

def print_green(text):
        print(Fore.GREEN + Style.BRIGHT + str(text) + Style.RESET_ALL )
        return


if __name__ == '__main__':
	main()