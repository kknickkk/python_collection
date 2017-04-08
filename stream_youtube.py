#!/usr/bin/python3

from subprocess import call

def main():

	title = argv[1]

	url = search(title)

	play(url)

def play(url):
	string = 'mpv (youtube-dl -f140 -g ' + url +')'
def search(title):

	
	