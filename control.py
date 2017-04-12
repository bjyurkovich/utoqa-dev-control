import serial
import sys


args = sys.argv[1:]
door = args[1]
command = args[0]


def fopen():
	return serial.Serial('/dev/ttyUSB0', 9600, timeout=1)


if door == 'LU' and command == 'open':
	speed = '30'
elif door == 'LU' and command == 'close':
	speed = '11'
else:
	speed = '100'

if door == 'RU' and command == 'open':
	speed = '30'
elif door == 'RU' and command == 'close':
	speed = '11'
else:
	speed = '100'

if command == 'open':
	comm = 'Q:#{0}:MTR:{1}\r'.format(door,'OP',speed)

if command == 'close':
	comm = 'Q:#{0}:MTR:{1}\r'.format(door,'CL',speed)

if command == 'status':
	comm = 'Q:#{0}:MTR:STATUS\r'.format(door)

if command == 'protocol':
	comm = '{0}\r'.format(args[1])

if command == 'led':
	comm = 'Q:#{0}:RGB:{1}:{2}:{3}\r'.format(door, args[2], args[3], args[4])

s = fopen()
s.write(comm)

reply = s.readline()

print reply