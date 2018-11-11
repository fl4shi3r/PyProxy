import re, os, environment, getpass, apt, npm, git



if os.geteuid() != 0:
    exit('You have to root privileges to run this script.\nPlease try again, this time using "sudo".\nExiting.')

host_ip = '172.31.1.4' #input('Enter the Proxy Host address: ')
host_port = '8080' # input('Enter the Proxy host port: ')

username = 'lit2017007' #input('Enter the username: ')
password_unhexed = '9044@Shiv'  #getpass.getpass(prompt='Enter the password: ')

pc_username ='fl4shi3r' #input('Enter the pc username: ')

def password_hex(password):
    hex_password = []
    for i in password:
        if i in ['@','!','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}',';',':','"',"'",',','<','.','>','/','?','`','~',' ']:
            hex_password.append('%' + str(hex(ord(i))[2:]))
        else:
            hex_password.append(i)
    return ''.join(hex_password)

password = password_hex(password_unhexed)

# environment.set_proxy(username,password , host_ip,host_port) // Set Proxy in Environment file
# environment.unset_proxy() // Unset Proxy in Environment file

# apt.set_proxy(username, password, host_ip, host_port)
# apt.unset_proxy()

# npm.set_proxy( username, password, host_ip, host_port, pc_username)
# npm.unset_proxy(pc_username)

# git.set_proxy(username, password, host_ip, host_port, pc_username )
# git.unset_proxy(pc_username)