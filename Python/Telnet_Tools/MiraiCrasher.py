#!/usr/bin/python

#! Imports !#
import os
import sys
import time
import getpass
import telnetlib

#! Declaring PC Username !#
user = getpass.getuser()

os.system("cls")

#! PRINT TERMS !#
try:
	file = open("C:\Users\\"+user+"\Desktop\Python\Telnet_Tools\Stinger\TOS.md", "r")

	for line in file:

		result_readme = os.path.isfile("C:\Users\\"+user+"\Desktop\Python\Telnet_Tools\Stinger\TOS.md")

		if result_readme == True:
			print(line)

except IOError:
	print("TOS.md Cannot be found. Exiting.")
	sys.exit()

time.sleep(4.5)

terms = raw_input("\r\nDo you agree to the ToS? (y/N): ")
if terms == 'y'.upper():
	print("Saving Input")

if terms == 'N'.lower():
	sys.exit("Failed to agree to terms of service.")

#! Checking if Files are Existing !#
os.system('cls')
time.sleep(2)
result = os.path.isfile("C:\Users\\"+user+"\Desktop\Python\Telnet_Tools\Stinger\Configuration\config.cfg")
if result == True:
	print("Configuration File... Found")
	time.sleep(2)

if result == False:
	print(+"Checking Configuration File... Missing")

#! Split Username : Password !#
file = open("C:\Users\\"+user+"\Desktop\Python\Telnet_Tools\Stinger\Configuration\config.cfg", "r")

for line in file:
	cfgIpv4 	   = line.split(":")[0]
	cfgUsername    = line.split(":")[1]
	cfgPayload     = line.split(":")[2]

print "IPAddress: %s " % (cfgIpv4)
print "Username: %s " % (cfgUsername)
print "Password: %s " % (cfgPayload)

#! Variables !#
hostname = cfgIpv4
username = cfgUsername
paylod = cfgPayload

time.sleep(3)
os.system('cls')

while 1:
	tn = telnetlib.Telnet(hostname)

	tn.read_until("login: ")
	tn.write(username + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(payload + "\n")

