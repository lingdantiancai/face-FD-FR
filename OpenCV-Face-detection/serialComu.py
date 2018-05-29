import serial
import time

def arduino_opendoor():
	try:
		ser = serial.Serial(
		    port = 'com4',
		    baudrate = 9600,
		    parity = serial.PARITY_NONE,
		    stopbits = serial.STOPBITS_ONE,
		    bytesize = serial.EIGHTBITS
		    )
	except:
		print('Something wrong in open serial port')
		return -1
	time.sleep(3)
	n = ser.write(b'1')
	ser.close()
	print(ser.isOpen())
	print('the signal for close the door has been sent')

# arduino_opendoor()