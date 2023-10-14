import os
import sys
import time
from time import sleep
import requests
from os import system

#This script is developed by prachanda.
#This is created for educational purposes only.
#You won't find anything to make this script work.You have to contact me first!

url = "https://citialerts.in/spoof/sendsms.php"
try:
	request = requests.get(url, timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] Oops, It looks like you have no Internet [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """
\033[1;32m ____    ____     ___     ___    _____  __   __
\033[1;32m/ ___|  |  _ \   / _ \   / _ \  |  ___| \ \ / /
\033[1;32m\___ \  | |_) | | | | | | | | | | |_     \ V /
\033[1;32m ___) | |  __/  | |_| | | |_| | |  _|     | |
\033[1;32m|____/  |_|      \___/   \___/  |_|       |_|  
\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m DEVELOPED BY akaprachan \033[1;31m(\033[1;33mprachanda\033[1;31m)
\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m MADE IN \033[1;31m(\033[1;33mNEPAL\033[1;31m)
"""
system("clear")
print (logo)
hprint(G + ' Starting Spoofy for Sending sms ...')
sleep(2)
print ("")
license = input(G + " Enter License Key" + C + " --> " + Y)
print ("")
name = input(G + " Enter Sender's ID" + C + " --> " + Y)
print ("")
recipient = input(G + " Enter Receiver's number(+1..)" + C + " --> " + Y)
print ("")

message = input(G + " Enter the Message" + C + " --> " + Y)
print("")


myobj = {
    'license': (None, license),
    'from': (None, name),
    'recipient': (None, recipient),
    'message': (None, message),
    'submit': (None, "submit"),
}
x = requests.post(url, files = myobj)
print(x.text)

response = requests.post('https://citialerts.in/spoof/sendsms.php', files=myobj)
hprint(C + ' Sending email to ' + recipient + ' ...')
print("")
print(G + " " + response.text)
print("")



if "BTC" in response.text:
    print(R + " Talk Live With Me --> https://t.me/akaprachanda")
else:
 print("")
