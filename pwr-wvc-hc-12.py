#!/usr/bin/python3
## Inverter id is "88ce"
## arg1 can be on, off, and a value between 01-64 (0-100%)

import sys
import serial
import binascii

ser = serial.serial_for_url('rfc2217://192.168.78.41:7000', timeout=1)

if len(sys.argv) < 2:
    print("Expected payload paramether!")
    sys.exit()

if sys.argv[1].lower() == 'on':
    ion = b'\xF3\xXX\xCE\x66\x00\x00\x00\x00' # inverter on
    ser.write(ion)
    s = ser.read(8)
    print("Turning On the Inverter ... :" , bytes(s).hex() , "-" , "OK!")
    f = open("/home/pi/wvc/wvc_stat", "w")
    f.write("1")
    f.close()
elif sys.argv[1].lower() == 'off':
    ioff = b'\xF4\x88\xCE\x67\x00\x00\x00\x00' # inverter off
    ser.write(ioff)
    s = ser.read(8)
    print("Turning Off the Inverter ... :" , bytes(s).hex() , "-" , "OK!")
    f = open("/home/pi/wvc/wvc_stat", "w")
    f.write("0")
    f.close()
else:
    print(sys.argv[1].lower())
    param = 'f188ce' + sys.argv[1].lower() + '00000000'
    ipwr = bytearray.fromhex(param)
    print(param)
    print(binascii.hexlify(bytearray(ipwr)).decode('ascii'))
    ser.write(ipwr)
    s = ser.read(8)
    print("Inverter Power Rate ... :" , bytes(s).hex() , "-" , "OK!")
    f = open("/home/pi/wvc/wvc_pwr", "w")
    f.write(sys.argv[1].lower())
    f.close()
