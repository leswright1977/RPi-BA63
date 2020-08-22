import time
import serial

ser=serial.Serial(
	port='/dev/ttyS0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

region = "\033R00"  #Set region to USA (Standard ASCII)
ser.write(region)

cls = "\033[2J" #send escape sequence to clear screen
ser.write(cls)


def cylon(delay):
	text = "*"
	while True:
		pos = 1
		for i in range(20):
			#Set position of character
			#see position cursor in manual ESC ‘[‘ ‘Py’ ; ‘Px’ ‘H’
			position = "\033[1;"+str(pos)+"H"
			ser.write(position+text)
			#delete previous character
			#see position cursor in manual ESC ‘[‘ ‘Py’ ; ‘Px’ ‘H’
			if pos > 1:
				delchar = "\033[1;"+str(pos-1)+"H"
				ser.write(delchar+" ")
			pos += 1
			time.sleep(delay)
		pos = 20

		#now do the same job backwards....
		for i in range(20):
			position = "\033[1;"+str(pos)+"H"
			ser.write(position+text)
			if pos < 20:
				delchar = "\033[1;"+str(pos+1)+"H"
				ser.write(delchar+" ")
			pos -= 1
			time.sleep(delay)


cylon(0.03)

	

ser.close
