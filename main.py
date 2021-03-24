import time

#Visit my github page for more!

runtime = time.time()


def watchui():
		global watchtime
		global watchstoptime
		input('Press enter to start the stopwatch')
		watchtime = time.time()
		input('Press enter to stop the stopwatch')
		watchstoptime = time.time()


watchui()

while True:
	try:
		response = int(input('''
		Time: %s
		Would you like to restart it? 
		1- Yes
		2- No
		''' % (watchstoptime - watchtime)))
	except ValueError:
		print('Please use one of the provided answers!')
		continue
	if response == 1:
		watchui()
		continue
	elif response == 2:
		quit("--- %s of runtime ---" % (time.time() - runtime))
