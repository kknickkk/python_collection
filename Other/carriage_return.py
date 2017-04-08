import time

def main():
	i = 0
	while i < 20:
		n = str(i)
		print("count: " + n, end='\r')
		time.sleep(1)
		i += 1

if __name__ == '__main__':
	main()
