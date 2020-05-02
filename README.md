# wvc-tool
WVC-Inverters Tool

wvc-tool.py Manual

build-in	AutoGet "modemID" ("FA")
		Default: Yes if "-m" is not selected.

		//	Payload	:	'\FA\xFF\xFF\xFF\xFF\xFF\xFF\x6D'
			Output	:	range '00000000-FFFFFFFF' : 'ser.read(8)	a.k.a "modemID"//

-o wvc.ini	Inverter's configuration file path. Multi Units.
		Default: "On", even if not selected in case "wvc.ini" named file located/detected in same folder.
		This option sub argument will define custom named configuration file's path.
		value of wvc.ini will be taken if "-o" is selected, but it's sub argument's missing.



-i WVCXXX/XXXX 	Inverter's Type/ID. Single unit.
		This Option is mandatory, if "-o" option's missing in front.
		It can be skipped if "-o" is selected, and a file defined or wvc.ini named file contains proper Inverter Type/ID entrys is located in the same folder.
		If not selected and "-o" is missing or it's cutom defined conf file's content is incorrect/corupted/syntax_errors etc.   it's sub argument is missing and the default "wvc.ini" file is missing or is empty or incomplete
		Print: "-i is a MANDATORY Option if "-o" isn't defined", folowed by the General Help.

		If selected, "Type/ID" must be defined, otherwise,
		Print: "You must define Type/ID".

		"Type"  - Inverter model from current "lookup" file:
		WVC295, WVC300, WVC350, WVC600, WVC850, WVC1200.

		"ID" 	- Inverter ID.
		Located on the Inverter.
		value range: 0000-FFFF


-d /dev/ttySXX	Optional. Phisical Serial device path. USB, RS232 etc.
		If selected, sub argument must be defined, otherwise,
		Print: "Device path must be defined'.
		Default is "On", even not selected, with "/dev/ttyUSB0:9600" as a default value.

		//	serialPort = serial.Serial("/dev/ttyUSB0", 9600)	//


-n IP:Port	Optional. Ser2net connection IP and Port.
		Requires "-o" or "-i".
		If "-n" is selected and "-o" or "-i" are not,
		Print: "-n requires "-o" or "-i" to be selected in front".
		If selected, "-d" sets "Off" and "physical" serial connection is replaced by "ser2net" connector.
		This option requires sub argument, otherwise,
		Print: "IP:Port" must be defined.

		//	serialPort = serial.serial_for_url('rfc2217://192.168.78.13:7000', timeout=1)	//


-m XXXXXXXX	Optional. Manual modemID (8)
		Default: Off - (Auto "FA")
		If selected, "FA" is skipped and it's variable "modemID", taken from here.
		Requires "-i", if not,
		Print: "-m requires -i to be selected in front"
		Sub argument must be defined, otherwise,
		Print: "modemID must be defined".
		values range: 00000000-FFFFFFFF


-s XX		Real time data Sample (17)
		Requires "-o" or "-i".
		If "-s" is selected and "-o" or "-i" are not,
		Print: "-s requires "-o" or "-i" to be selected in front".
		Optional sub argument: value range: 1-99
		It is the number of cicles to be rolled and infinity loop if sub argument is missing.
		//	Payload : 'F2<modemID><ID>65'
			Output	: ser.read(17)

		DevOpsOnly: Working "Realtime Stats"

		//	Payload:	'\xf2\xfb\x04\x11\xe3\x88\xce\x65'	//


-p xxxx		Inverter Power Switch.
		Requires "-o" or "-i".
		If "-p" is selected and "-o" or "-i" are not,
		Print: "-p" requires "-o" or "-i" to be selected in front".
		sub argument must be defined if "-p" is selected, otherwise,
		Print: "action for "-p" must be selected. on, off or restart

		// Payloads:		

		on	=	'F3<modemID><InverterID>66'
		on_Output:		'F3<modemID><InverterID>66' : ser.read(8) = OK. Done. Command Accepted.

		off	=	'F4<modemID><InverterID>67'
		off_Output:		'F4<modemID><InverterID>67' : ser.read(8) = OK. Done. Command Accepted.

		restart	=	'off+sleep5+on'	//


-b MQttIP:Port	Data collection and MQtt publisher.
		Requires "-o" or "-i".
		If "-b" is selected and "-o" or "-i" are not,
		Print: "-b requires "-o" or "-i" to be selected in front".
		If sub argument is missing,
		Print: Inverter Real data Infinity cicles.
		//	Payload:	'F5<modemID><InverterID>68'
			Output:		ser.read(28)	//


-r		Optional. Resets Inverter's Power-Meter Counter

		//	Payload:	'F0<modemID><InverterID>00'
			Output:		'F0<modemID><InverterID>00' : ser.read(8) = OK. Command Accepted.


-a XX		Adjust Output's (AC) Power.
		values range: 01-64 (64=100%)
		
		//	Payload:	'F1<modemID><InverterID><01-64>'
			Output:		'F1<modemID><InverterID><The same return value>' : ser.read(8) = OK. Command Accepted.


-w XX		Optional. Adds a delay in Cicle's begining.
		Default: Off
		Requires -b or -s if selected, and ofcource "-o" or "-i" selected in front.
		value range 1-99 (sec)

-l wvc.log	Optional. Custom Log filename path.
		If sub argument's missing will creare wvc.log in same filder.
		Default: "Off"


-h		Help. This Screen.

