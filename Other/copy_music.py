#!/usr/local/bin/python
from glob import glob
from subprocess import call, check_output
from glob2 import glob as glob2
import mylib as ml
import os
import time

start_time = time.time()
DEBUG = False
print("Debug is: " + str(DEBUG))

# read destination folders
# read source folders
# remove unwanted folders
# remove excess folders from dest
# create missing folders in  dest
# use glob2 to find mp3
# copy mp3 non in dest
# convert non mp3 files
# remove not in source mp3

#music_path = '/Users/Nick/Desktop/Music/'
music_path = '/Volumes/Data HD/Music/iTunes/iTunes Media/Music/'
usb_path2 = '/Volumes/NO_NAME/Music/' 	# phone
usb_path1 = '/Volumes/SANDISK/Music/' 	# Car USB 
choice = int(input("Please select destination:\n1) Car USB " + usb_path1 + "\n2) Phone " + usb_path2 + "\n"))
if choice == 1:
	usb_path = usb_path1
elif choice == 2:
	usb_path = usb_path2
else:
	ml.print_red("Invalid option!\n Exiting...")
	exit()

#				0 				1				2			3				4
#statistics = [added_songs, deleted_songs, added_folders, deleted_folders, converted_files]
statistics = [0,0,0,0,0]

excluded_folders = [music_path + 'Hans Zimmer',music_path + 'Marconi Union']

def main():
	ml.print_green('Hola! Starting Program...')
	music_f = glob(music_path + '*')
	usb_f = glob(usb_path + '*')
	
	music_f = remove_unwanted(music_f, excluded_folders)
	remove_excess_folders(music_f, usb_f)
	create_missing_folders(music_f, usb_f)
	music_mp3 = create_music_mp3()
	music_m4a = create_music_m4a()
	usb_mp3 = glob2(usb_path + '*/**/*.mp3')
	ml.print_green('Source: ' + str(len(music_mp3)) + ' .mp3 and ' + str(len(music_m4a)) + ' .m4a')
	ml.print_green('Destination ' + str(len(usb_mp3)) + ' .mp3')
	remove_old_mp3(music_mp3, music_m4a, usb_mp3)
	copy_mp3(music_mp3, usb_mp3)
	convert_m4a(music_m4a, usb_mp3)

	print_statistics()
	ml.execution_time(start_time)
	return

def create_music_mp3():
	music_mp3 = glob2(music_path + '*/**/*.mp3')
	newlist = list(music_mp3)
	for item in excluded_folders:
		itemsplit = item.split('/')
		for submp3 in newlist:
			split = submp3.split('/')
			if(split[7] == itemsplit[7]):
				music_mp3.remove(submp3)
	return music_mp3

def create_music_m4a():
	music_m4a = glob2(music_path + '*/**/*.m4a')
	newlist = list(music_m4a)
	for item in excluded_folders:
		itemsplit = item.split('/')
		for subm4a in newlist:
			split = subm4a.split('/')
			if(split[7] == itemsplit[7]):
				music_m4a.remove(submp3)
	return music_m4a

def print_statistics():
	flag = 1
	for i in statistics:
		if i == 1:
			flag = 0
	if flag == 1:
		ml.print_green('\t\t-------- NO CHANGES MADE --------')
		return

	ml.print_green('\t\tAdded\t\t\t' + str(statistics[0]) + ' songs, ' + str(statistics[2]) + ' folders')
	ml.print_green('\t\tConverted and added\t' + str(statistics[4]) + ' files')
	ml.print_red('\t\tDeleted\t\t\t' + str(statistics[1]) + ' songs, ' + str(statistics[3]) + ' folders')
	

def remove_old_mp3(music_mp3, music_m4a, usb_mp3):
	for item in usb_mp3:
		if item.replace(usb_path, music_path) not in music_mp3:
			s = item.replace(usb_path, music_path)
			s = s[:len(s) - 3] + 'm4a' 
			if s not in music_m4a:
				statistics[1] += 1
				ml.print_red('Removing ' + item)
				if not DEBUG:
					call(['rm', item])

def convert_m4a(music_m4a, usb_mp3):
	try:
		call(['rm', 'temp.mp3'])
	except:
		pass

	for item in music_m4a:
		f_in = item
		temp = check_output(['pwd']).decode().strip('\n')

		l = glob(temp + '/*')
		temp = temp + '/temp.mp3'
		f_out = item.replace(music_path, usb_path)
		f_out = f_out[:len(f_out) - 3] + 'mp3'
		if f_out not in usb_mp3:
			ml.print_green("Converting: " + f_in)
			statistics[4] += 1
			if not DEBUG:
				call(['ffmpeg','-loglevel', 'quiet','-i', f_in, '-acodec', 'libmp3lame', '-ab', '128k', temp])
				call(['mv', temp, f_out])

def copy_mp3(music_mp3, usb_mp3):
	for item in music_mp3:
		if item.replace(music_path, usb_path) not in usb_mp3:
			statistics[0] += 1
			ml.print_green('Copying ' + item.strip(music_path))
			if not DEBUG:
				call(['cp', item, item.replace(music_path, usb_path)])

def create_missing_folders(music_f, usb_f):

	for item in music_f:
		dest = item.replace(music_path, usb_path)
		
		if dest not in usb_f:
			statistics[2] += 1
			
			ml.print_green('Creating ' + dest)
			if not DEBUG:
				call(['mkdir', dest])

		#print("M: " + item)
		#print("D:" + dest)
		subfolders_m = glob(item + '/*')
		subfolders_d = glob(dest + '/*')

		for sub in subfolders_m:
			tras = sub.replace(music_path, usb_path)
			#print("---> " + sub)
			#print(subfolders_m)
			if tras not in subfolders_d:
				ml.print_red("Should be creating " + tras)
				statistics[2] += 1
				if not DEBUG:
					call(['mkdir', tras])

def remove_excess_folders(music_f, usb_f):
	for item in usb_f:
		if item.replace(usb_path, music_path) not in music_f:
			statistics[3] += 1
			ml.print_red("Removing " + item)
			if not DEBUG:
				call(['rm', '-r', item])
	

def remove_unwanted(music_f, excluded_folders):
	for item in music_f:
		if item in excluded_folders:
			music_f.remove(item)
	return music_f 

if __name__ == '__main__':
		main()	