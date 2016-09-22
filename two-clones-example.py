import paramiko
import time

def disable_paging(remot_conn):
  "Disable paging, unkown, part of the example"

  #Clear the buffer on the screen
  #output = remote_conn.recv(1000)

  return output

if __name__=='__main__':

 #VARIABLES THAT NEED TO BE CHANGED
 ip = '10.0.2.10'
 username = 'raba'
 password = 'sneakers123'

 # Create instance of SSHClient objec
 remote_conn_pre = paramiko.SSHClient()

 #Automatically add untrusted hosts (make sure okay for security policy in your environment)
 remote_conn_pre.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

 #initiate SSH connection
 remote_conn_pre.connect(ip,username=username,password=password,look_for_keys=False,allow_agent=False)
 print "SSH connection established to %s" % ip

 #Use invoke_shell to establish an 'interactive session'
 remote_conn = remote_conn_pre.invoke_shell()
 print "Interactive SSH session established"

 #Strip the intial router prompt
 output = remote_conn.recv(1000)

 #See what we have
 print output

 #Test a command
 remote_conn.send("\n")
 remote_conn.send("ls\n")

 #Wait for the command to complete
 time.sleep(2)

 output = remote_conn.recv(5000)
 print output

 remote_conn.send("nohup ./firefox_basic.sh & \n")
 time.sleep(2)
 remote_conn.close()
 
 ip = '10.0.2.12'
 username = 'mobo'

 remote_conn_pre.connect(ip,username=username,password=password,look_for_keys=False,allow_agent=False)
 remote_conn = remote_conn_pre.invoke_shell()
 remote_conn.send("nohup ./firefox_basic.sh & \n")
 ouput = remote_conn.recv(5000)
 print output
