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

sometext0 = '  BA63 RPi Display!'
sometext1 = '.,,:;||;:,,..,,:;||;:,,.'

ser.write(line1+sometext0)


#scroll to the right scrolltext = scrolltext[-1] + scrolltext[0:-1] 

def scroll(scrolltext,delay):
	if len(scrolltext)<19:
		#Check if the text is shorter than the display, if it is, pad it with spaces
		padding = " " * (20-len(scrolltext))
		scrolltext = scrolltext+padding

	while True:
		#scroll to the left
		#remove the char at the 0th position and tack on the end
		scrolltext = scrolltext[1:]+scrolltext[0]
		printable_chars = scrolltext
		#only try to display the portion of the text that will fit on the display!
		if len(scrolltext)>19:
			printable_chars =scrolltext[0:20]
		ser.write(line2+printable_chars)
		time.sleep(delay) #set scroll speed

scroll(sometext1,0.1)

ser.close
