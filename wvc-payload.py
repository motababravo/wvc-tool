#!/usr/bin/python3

# Load libraryes
import sys
import serial

# Gets the command line parameter and replace "\x" with empty string
# we just need only pure HEX formatted string
# for example \xf2\xfb\x04\x11\xe3\x88\xce\x65 will be converted to f2fb0411e388ce65
# After that we convert the HEX string to byte array
payLoad = bytearray.fromhex(sys.argv[1].lower().replace("\\", "").replace("x", ""))

# Open serial port
#serialPort = serial.serial_for_url('rfc2217://192.168.78.13:7000', timeout=1)
serialPort = serial.Serial("/dev/ttyUSB0", 9600)

# Send payLoad adta to modem
serialPort.write(payLoad)

# Gets result from serial port
receiedData = serialPort.read(17)

# Print received result on screen
print(bytes(receiedData).hex())
