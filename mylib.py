from colorama import Fore, Back, Style
import time

def print_red(text):
        print(Fore.RED + Style.BRIGHT+ str(text) + Style.RESET_ALL )
        return

def print_green(text):
        print(Fore.GREEN + Style.BRIGHT + str(text) + Style.RESET_ALL )
        return

# call start_time = time.time()

def execution_time(start_time):
	execution_seconds =  int((time.time() - start_time))
	execution_minutes = execution_seconds / 60
	execution_hours = execution_minutes / 24
	minutes = execution_minutes - execution_hours * 24
	seconds = execution_seconds - execution_minutes * 60
	print_green("Execution time: " + str(execution_hours) + ' hours ' + str(minutes) +  ' minutes ' + str(seconds) + ' seconds')
