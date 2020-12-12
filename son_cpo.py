import requests
import datetime
from time import strftime 
from itertools import chain
s = requests.Session()

#login_url: please provide user crendentials created for market specific
login_url = "http://10.127.194.45:5000/api/v1/system/auth/backends/internal/login/?username=<>&password=<>"

#API to get markets
#market_url = "http://10.127.194.45:5000/api/v1/system/markets/?page=0&page_size=50&tz=%22Asia%2FKolkata%22"
market_url = "http://10.127.194.45:5000/api/v1/system/markets/?fields=%5B%22name%22%5D&page=0&page_size=50&tz=%22Asia%2FKolkata%22"
#API to get OSS
oss_url ="http://10.127.194.45:5000/api/v1/network/oss/config/?fields=%5B%22name%22,%22_type%22,%22vendor%22,%22rat%22%5D&format=%22rich%22&tz=%22Asia%2FCalcutta%22"

#API to get sw version

#Handling response
login_response = s.post(login_url)

#reading response for market
r = s.get(market_url)
#######Heading######
print "SON Report"

#storing data
market_name = r.json()
market_count = market_name.get('count')
marker_list = []
i=0
for market_o in market_name.get('objects'):
	i=i+1
	print "market" + i + market_o['name']
print "No: of market available:" +  market_count

#reading response for OSS
oss_r = s.get(oss_url)
oss_name = oss_r.json()
oss_count = oss_name.get('count')
oss_list = []
j=0
for oss_in in oss_name.get('objects'):
	j=j+1
	print "name" + j + oss_in['name']
	print "vendor" + j + " is" + oss_in['vendor']
print "total oss count is " + oss_count
#print market_names
#print ("markets: ",market)


import pexpect
child = pexpect.spawn ('mp')
child.expect ('User: ')
child.sendline ('admin')
child.expect ('Password:')
child.sendline ('admin')
child.expect ('-> ')
child.sendline ('3')
child.expect('-Markets-> ')
child.sendline ('1')
child.expect('ftp> ')
child.sendline ('bye')


import pexpect
child = pexpect.spawn ('mp')
child.timeout=300
child.expect ('Please insert API credentials:')
child.sendline ('')
child.expect ('User: ')
child.sendline ('admin')
child.expect ('Password:')
child.sendline ('admin')
child.expect ('-> ')
child.sendline ('3')
child.expect('-Markets-> ')
child.sendline ('1')
child.expect('ftp> ')
child.sendline ('bye')

expect "Enter the number1 :" { send "12\r" }
expect "Enter the number2 :" { send "23\r" }
expect "User: " {send ""}

import pexpect
child = pexpect.spawn ('/intucell/latest/bin/python /intucell/maintenance_portal_6/maintenance_portal.pyc')
child.timeout=60
child.expect ('User: ')
child.sendline ('admin')
child.expect ('Password:')
child.sendline ('admin')
child.expect ('-> ')
child.sendline ('3')
child.expect('-Markets-> ')
child.sendline ('1')

import pexpect
import sys
child = pexpect.spawn ('/intucell/latest/bin/python /intucell/maintenance_portal_6/maintenance_portal.pyc')
child.logfile =  open("/tmp/mylog", "w")
child.expect ('Please insert API credentials:')
child.sendline ('')
child.expect ('User: ')
child.sendline ('admin')
child.expect ('Password: ')
child.sendline ('admin')
child.expect ('-> ')
child.sendline ('3')
child.expect('-Markets-> ')
child.sendline ('1')
child.expect('-Markets-> ')
child.sendline ('q')

print child.read())


~
