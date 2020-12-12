#usr/bin/python
#########################
### Libraries Used
#########################
import socket
import time
import getpass
import sys
import paramiko
import re
import os
import StringIO
#HOST = "10.127.194.27"


# Port used for ssh
PORT=22
# Setting the timeout duration
TIMEOUT=10
#Output string
OUTPUT=("\n")

def validateSsh(hostname, port, filePath):
        try:
                socket.inet_aton(hostname)
        except socket.error:
                sys.exit("Please enter a valid IP Address")
        response = os.system("ping -c 1 > /dev/null " + hostname)
        if response != 0:
                sys.exit("Host Unreachable")
        return 0
        try:
                fileObj = open(filePath, 'rU')
        except:
                sys.exit("Invalid File Path")
        return ssh


#Take inputs from the user for Hostname, Username and Password
hostname = raw_input("Enter the hostname: ")
user = raw_input("Enter your remote account: ")
password = getpass.getpass()
filePath = raw_input("Enter the file path where commands are stored: ")

# Text File that contains the commands
ssh = validateSsh(hostname, PORT, filePath)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=user, password= password)
print ("Ssh Done")

fileObj = open(filePath,'rU')
commands=fileObj.read()
fileObj.close()

OUTPUT= ["\n"]
commandList=commands.split("\n")
time.sleep(10)
for readLine in commandList:
        print "command:",readLine
        stdin, stdout, stderr = ssh.exec_command(readLine + "\n")
        line = stdout.readlines()
        print line
        print stderr.readlines()
        OUTPUT += [line]
ssh.close()

dateTime = time.strftime("%d/%m/%Y %H:%M:%S")
outputFile=open("output.txt", "a")
outputFile.write("\n")
outputFile.write("------------------------------------------------")
outputFile.write("DateTime: " + dateTime)
outputFile.write("------------------------------------------------")
outputFile.write("\n")
outputFile.write(str(OUTPUT))
print ("Run Successful")
outputFile.close()
