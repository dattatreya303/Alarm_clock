from __future__ import print_function
import sys
import getopt
import datetime
import webbrowser
from random import randrange
import time

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "Hh:m:s:", ["help"])
	except getopt.GetoptError:
		# print("%$^&#")
		print("Use [-h] [-m] [-s] in 24-hour format")
		sys.exit(2)

	print(argv)
	H = 0
	M = 0
	S = 0
	for flag, arg in opts:
		# print '^\n'
		if(flag == '-h'):
			H = arg
		elif(flag == '-m'):
			M = arg
		elif(flag == '-s'):
			S = arg
		elif(flag in ('-H', '--help')):
			print("Help: Use [-h] [-m] [-s] in 24-hour format")
			sys.exit(2)

	# playlist = "".join(args)

	while True:
		# print '*\n'
		now_time = datetime.datetime.now()
		if str(now_time.hour) == H and str(now_time.minute) == M and str(now_time.second) == S:
			file = open('playlist.txt', 'r')
			c = randrange(3)
			i=0
			for line in file:
				if i == c:
					webbrowser.open(str(line), new=2)
					break
				i += 1
			time.sleep(10)
		else:
			sys.stdout.write("\rCurrent time is " + str(now_time.hour) + str(now_time.minute) + str(now_time.second) + ". Alarm will start at " + H + M + S + ".")

if __name__ == '__main__':
	main(sys.argv[1:])