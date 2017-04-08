#!/usr/bin/python3
import telegram
from random import randint
import subprocess
from os import environ

#in /etc/inittab put uniq:3:respawn:/path/to/script

TOKEN = '250008562:AAEZvprHPvtDQrV0IDkRSPc6peqXYUdLsjg'
chatid = 85048573
bot = telegram.Bot(TOKEN)

def main():
	
	ip = get_ip()

	num = randint(1000,9999)
	text = 'Log in detected, enter this number:\n' + str(num) + '\n'
	bot.sendMessage(chatid, text)
	ans = int(input('Enter received message\n'))
	if ans == num:
		print('Correct code! You may proceed')
	else:
		#abort ssh connection
		pid_command = 'who -u'
		pid = subprocess.check_output(pid_command.split())
		pid = pid.decode()
		pid = pid.split()
		index = pid.index('(' + ip + ')')
		pid_number = pid[index - 1]
		# as root
		kill_ssh_command = 'kill ' + pid_number
		subprocess.call(kill_ssh_command.split())
		
		pass


def get_ip():
	log_data = environ['SSH_CLIENT']
	log_data = log_data.split(' ')
	ip_addr = log_data[0]
	return ip_addr

if __name__ == '__main__':
		main()	