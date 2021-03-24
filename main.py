import time

#Visit my github page for more!

runtime = time.time()


def watchui():
    global watchtime
    input('Press enter to start the stopwatch')
    watchtime = time.time()
    input('Press enter to stop the stopwatch')


watchui()

while True:
    try:
        response = int(
            input('''
		 Time: %s

		 Would you like to restart it?
		 
		 1- Yes
		 2- No
		 ''' % (time.time() - watchtime)))
    except ValueError:
        print('Please use one of the provided answers!')
    if response == 1:
        watchui()
        continue
    elif response == 2:
        quit("--- %s of runtime ---" % (time.time() - runtime))
