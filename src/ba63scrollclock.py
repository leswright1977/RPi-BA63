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

string1 = "~~~~~~Les' Lab~~~~~~"
ser.write(line1+string1)
string2 = "~Raspberry Pi Clock~"
ser.write(line2+string2)

time.sleep(3)

ser.write(cls)


scrolltext = '.,,:;||;:,,..,,:;||;:,,.'

def scroll(scrolltext,delay):
	spinner = '|/-\|/-' 
	spin = 0

	#Check if the text is shorter than the display, if it is, pad it with spaces
	if len(scrolltext)<19:
		padding = " " * (20-len(scrolltext))
		scrolltext = scrolltext+padding

	while True:
		now = datetime.now()
		now = now.strftime("%Y-%m-%d %H:%M:%S")
		ser.write(line1+now+spinner[spin])
		spin+=1
		#reset the spinner
		if spin > len(spinner)-1:
			spin = 0
		#scroll to the left
		#remove the char at the 0th position and tack on the end
		scrolltext = scrolltext[1:]+scrolltext[0]
		printable_chars = scrolltext

		#only try to display the portion of the text that will fit on the display!
		if len(scrolltext)>19:
			printable_chars =scrolltext[0:20]
		ser.write(line2+printable_chars)
		time.sleep(delay) #set scroll speed

scroll(scrolltext,0.1)
	
ser.close
