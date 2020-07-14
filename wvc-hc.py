#!/usr/bin/python3

# Load libraryes pyserial is required (pip install piserial)
import sys
import serial
import paho.mqtt.publish as publish

varMQttBrk = "192.168.78.13"
varMQtopic = "solar/HC-12/88ce"


def Lookup(pathToLookupFile, searchString):
    searchLen = len(searchString)
    with open(pathToLookupFile) as search:
        for line in search:
            if line[0:searchLen] == searchString:
                line = line.rstrip()
                return line[searchLen + 1:]

if len(sys.argv) < 2:
    print("Expected payload paramether!")
    sys.exit()

# Gets the command line parameter as HEX, for example f288ce6500000000 and
# convert to byte array
param = sys.argv[1].lower();
payLoad = bytearray.fromhex(param)


# Open serial port
#serialPort = serial.serial_for_url('rfc2217://192.168.78.13:7000', timeout=1)
serialPort = serial.Serial("COM6", 9600)

# Send payLoad data to modem
serialPort.write(payLoad)

# Gets result from serial port
receiedData = serialPort.read(19)
#receiedData = bytearray.fromhex("f288ce6500005c001501290017014b00000000")

if receiedData:
    # Expected result is f288ce6500005c001501290017014c00000000 (example)
    # First 12 chars (suffix) from receiedData (in this example f288ce650000) are equal to fisr 12 chars from command line param (payload)
    # The last 8 chars (prefix) (in this example 00000000) are equal to last 8 chars from command line param (payload)
    output = bytes(receiedData).hex()
    
    if len(output) == 38 and output[0:12] == param[0:12] and output[-8:] == param[-8:]:
        # Build lookup search string for temperature. The temperature byte is located imediatle befor prefix sequence, in this example just before 00000000 
        temperatureHEXByte = output[28:30]
        temperature = str(int(temperatureHEXByte, 16))
        print("temperatureHEXByte: " + temperatureHEXByte + ", DEC: " + temperature)
        print("Device temperature: " + Lookup("lookup_WVC600", "TMP" + temperature))
#        publish.single(varMQtopic + "/temp", Lookup("lookup_WVC600", "TMP" + temperature), hostname=varMQttBrk)
        
        # Build lookup string for Volt AC. This data is located before temperature and has a length of 2 bytes - need to be reversed
        voltACHEXByte = output[24:28]        
        voltACHEXByte = voltACHEXByte[2:4] + voltACHEXByte[0:2]
        voltAC = str(int(voltACHEXByte, 16))        
        print("voltACHEXByte: " + voltACHEXByte + ", DEC: " + voltAC)
        print("Device AC Voltage: " + Lookup("lookup_WVC600", "VAC" + voltAC))
#        publish.single(varMQtopic + "/vac", Lookup("lookup_WVC600", "VAC" + voltAC), hostname=varMQttBrk)

        # Build lookup string for Amper AC. This data is located before Volt AC and has a length of 2 bytes - need to be reversed
        amperACHEXByte = output[20:24]        
        amperACHEXByte = amperACHEXByte[2:4] + amperACHEXByte[0:2]
        amperAC = str(int(amperACHEXByte, 16))        
        print("amperACHEXByte: " + amperACHEXByte + ", DEC: " + amperAC)
        print("Device AC Ampers: " + Lookup("lookup_WVC600", "AACB" + amperAC))


        # Build lookup string for Volt DC. This data is located before Amper AC and has a length of 2 bytes - need to be reversed
        voltDCHEXByte = output[16:20]        
        voltDCHEXByte = voltDCHEXByte[2:4] + voltDCHEXByte[0:2]
        voltDC = str(int(voltDCHEXByte, 16))        
        print("voltDCHEXByte: " + voltDCHEXByte + ", DEC: " + voltDC)
        print("Device DC Voltage: " + Lookup("lookup_WVC600", "VDC" + voltDC))


        # Build lookup string for Amper DC. This data is located before Volt DC and has a length of 2 bytes - need to be reversed
        amperDCHEXByte = output[12:16]        
        amperDCHEXByte = amperDCHEXByte[2:4] + amperDCHEXByte[0:2]
        amperDC = str(int(amperDCHEXByte, 16))        
        print("amperDCHEXByte: " + amperDCHEXByte + ", DEC: " + amperDC)
        print("Device DC Ampers: " + Lookup("lookup_WVC600", "ADC" + amperDC))


    else:
        print("Invalid output")
else:
    print("Empty receiedData")
    

