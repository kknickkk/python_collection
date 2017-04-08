#!/usr/local/bin/python3
from subprocess import call
import shlex
print("Remember to call the function in the folder! (Limited functionality of ffmpeg)")
film_path = input("Enter film path: ")
sub_path = input("Enter sutitle path: ")
out_name = "'SUB_" + film_path + "'"
film_path = "'" + film_path + "'"
sub_path = "'" + sub_path + "'"
out_name = 'SUB_' + film_path
command = "ffmpeg -i " + film_path + " -i " + sub_path + " -c:v copy -c:a copy -c:s mov_text -metadata:s:s:0 language=eng " + out_name
command = shlex.split(command)
call(command)
