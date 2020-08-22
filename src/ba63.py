import time
from datetime import datetime
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


cls = "\033[2J" #send escape sequence to clear screen!
ser.write(cls)

line1 = "\033[1;1H" #Escape seqence to start on line 1 char 1
line2 = "\033[2;1H" #Escape seqence to start on line 2 char 1

string1 = "     -Les' Lab-     "
ser.write(line1+string1)
string2 = "...................."
ser.write(line2+string2)

time.sleep(10)

ser.write(cls)

ser.close()
