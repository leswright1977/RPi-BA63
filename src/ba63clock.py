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


cls = "\033[2J" #send escape sequence to clear screen
ser.write(cls)

line1 = "\033[1;1H" #Escape seqence to start on line 1 char 1
line2 = "\033[2;1H" #Escape seqence to start on line 2 char 1

#splash screen
string1 = "~~~~~~Les' Lab~~~~~~"
ser.write(line1+string1)
string2 = "~Raspberry Pi Clock~"
ser.write(line2+string2)
time.sleep(3)

ser.write(cls)

#clock and spinner!
spinner = '|/-\|/-'
spin = 0

while True:
	
	now = datetime.now()
	now = now.strftime("%Y-%m-%d %H:%M:%S")
	ser.write(line1+now+spinner[spin])
	time.sleep(0.001)
	
	
	unixtime = str(round(time.time(),1))
	ser.write(line2+"    "+unixtime)
	

	spin+=1
	if spin > len(spinner)-1:
		spin = 0


ser.close
