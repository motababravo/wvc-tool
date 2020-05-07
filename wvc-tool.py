#!/usr/bin/python3

# Argparse, command-line options
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fork", help="Run in background")
parser.add_argument("-q", "--quiet", help="Cuts All on-screen output")
parser.parse_args()

import serial
# Local
ser = serial.Serial("/dev/ttyUSB0", 9600)
# Remote (Ser2Net)
# ser = serial.serial_for_url('rfc2217://192.168.78.13:7000', timeout=1)

# AutoGet Modem ID
getmid = b'\xFA\xFF\xFF\xFF\xFF\xFF\xFF\x6D' # get modem ID
ser.write(getmid)
s = ser.read(8)
#print(s)
#print(bytes(s).hex())
id = s [1:-3]
#print("Reading modem ID ... :" , bytes(id).hex())
print(bytes(id).hex())
