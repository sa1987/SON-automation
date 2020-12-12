
import pexpect
import sys
child = pexpect.spawn("bash")
child.logfile = sys.stdout
child.sendline('ssh user@example.com')
child.expect('(?i)password')
child.sendline(mypassword)
child.sendline('/intucell/latest/bin/python /intucell/maintenance_portal_6/maintenance_portal.pyc')
#child.logfile = open("/tmp/mylog", "w")
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


import pexpect
import sys
child = pexpect.spawn("bash")
child.logfile = sys.stdout
child = spawn('ssh user@example.com:.')
child.expect('(?i)password')
child.sendline(mypassword)
child.expect(' cd /intucell/latest/bin/python /intucell/maintenance_portal_6/')

#child.logfile = open("/tmp/mylog", "w")
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