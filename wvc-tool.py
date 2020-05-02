#!/usr/bin/python3

import serial
ser = serial.Serial("/dev/ttyUSB0", 9600)
###ser = serial.Serial("COM5", 9600)

getmid = b'\xFA\xFF\xFF\xFF\xFF\xFF\xFF\x6D' # get modem ID
ser.write(getmid)
s = ser.read(8)
#print(s)
##print(bytes(s).hex())
id = s [1:-3]
#print("Reading modem ID ... :" , bytes(id).hex())
print(bytes(id).hex())
