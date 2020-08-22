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



def dualscroll(scrolltext1,scrolltext2,delay):
	#Check if the text is shorter than the display, 
	#if it is, pad it with spaces
	if len(scrolltext1)<19:
		padding = " " * (20-len(scrolltext1))
		scrolltext1 = scrolltext1+padding
	if len(scrolltext2)<19:
		padding = " " * (20-len(scrolltext2))
		scrolltext2 = scrolltext2+padding

	while True:
		#scroll to the left
		#remove the char at the 0th position and tack on the end
		scrolltext1 = scrolltext1[1:]+scrolltext1[0]
		printable_chars1 = scrolltext1

		scrolltext2 = scrolltext2[1:]+scrolltext2[0]
		printable_chars2 = scrolltext2

		#only try to display the portion of the text that will fit on the display!
		if len(scrolltext1)>19:
			printable_chars1 =scrolltext1[0:20]

		if len(scrolltext2)>19:
			printable_chars2 =scrolltext2[0:20]

		ser.write(line1+printable_chars1)
		ser.write(line2+printable_chars2)
		time.sleep(delay) #set scroll speed

text1 = '     .,:|||:,.     '
text2 = '..,:|||||||||||:,..'

dualscroll(text1,text2,0.1)



ser.close
