#!/usr/bin/python

from __future__ import print_function
from random import randrange
import sys, getopt, datetime, webbrowser, time

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "Hh:m:", ["help"])
	except getopt.GetoptError:
		# print("%$^&#")
		print("Use [-h] hours [-m] minutes in 24-hour format")
		sys.exit(2)

	# print(argv)
	H = 0
	M = 0
	for flag, arg in opts:
		# print '^\n'
		if(flag == '-h'):
			H = arg
		elif(flag == '-m'):
			M = arg
		elif(flag in ('-H', '--help')):
			print("Help: Use [-h] hours [-m] minutes in 24-hour format")
			sys.exit(2)

	# print(H)
	l = 0
	while True:
		try:
			# print '*\n'
			now_time = datetime.datetime.now()
			p = time.strftime("%p")
			c = 0
			if (p == 'AM' and int(H) < 12 and now_time.hour == int(H)) or (p == 'PM' and int(H) >= 12 and now_time.hour == int(H)-12):
				c = 1
			# print(c)
			l = randrange(3)
			if now_time.minute == int(M) and now_time.second == 0 and c == 1:
				file = open('playlist.txt', 'r')
				i=0
				for line in file:
					if i == l:
						webbrowser.open(str(line), new=2)
						break
					i += 1
				time.sleep(10)
			else:
				p = ''
				h = 0
				if int(H) >= 12:
					h = int(H) - 12 
					p = 'PM'
				else:
					h = int(H)
					p = 'AM'
				sys.stdout.write("\rCurrent time is " + time.strftime("%H:%M:%S %p") + ". Alarm will start at " + str(h) + ":"  + str(M) + " " + p + ".")
		except KeyboardInterrupt:
			print("\nAlarm stopped.")
			sys.exit(2)

if __name__ == '__main__':
	main(sys.argv[1:])