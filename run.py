#!/usr/bin/env python3

from dwinlcd import DWIN_LCD
import signal
import sys

def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

# define the interface pins and serial port on the raspberry pi

encoder_Pins = ("PL3", "PL2")
button_Pin = "PL8"

LCD_COM_Port = '/dev/ttyS3'

# Read the api key from a local file named apikey.txt
try:
        f = open("/home/pi/DWIN_T5UIC1_LCD/apikey.txt")
        API_Key = (f.read()).strip()
except:
       sys.exit("Cannot read the api key please make sure the file exists")

# Init the lcd driver
DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key
)
