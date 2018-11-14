import re, os, environment, getpass, apt, npm, git, gsetting, bash, dnf



if os.geteuid() != 0:
    exit('You have to root privileges to run this script.\nPlease try again, this time using "sudo".\nExiting.')

def password_hex(password):
    hex_password = []
    for i in password:
        if i in ['@','!','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}',';',':','"',"'",',','<','.','>','/','?','`','~',' ']:
            hex_password.append('%' + str(hex(ord(i))[2:]))
        else:
            hex_password.append(i)
    return ''.join(hex_password)

choice = input('1.set proxy\n2.unset proxy\nEnter your choice(1/2): ')
if choice == '1':
    host_ip = input('Enter the Proxy Host address: ')
    host_port = input('Enter the Proxy host port: ')

    username = input('Enter the username: ')
    password_unhexed = getpass.getpass(prompt='Enter the password: ')
    password = password_hex(password_unhexed)
    
    pc_username = input('Enter the pc username: ')
    
    # environment.set_proxy(username,password , host_ip,host_port) 
    # apt.set_proxy(username, password, host_ip, host_port)
    # npm.set_proxy( username, password, host_ip, host_port, pc_username)
    # git.set_proxy(username, password, host_ip, host_port, pc_username )
    gsetting.set_proxy(username, password, host_ip, host_port, pc_username)
    # bash.set_proxy(username, password, host_ip, host_port, pc_username)
    # dnf.set_proxy(username, password, host_ip, host_port)

elif choice == '2':
    pc_username = input('Enter the pc username: ')

    # environment.unset_proxy() 
    # apt.unset_proxy()
    # npm.unset_proxy(pc_username)
    # git.unset_proxy(pc_username)
    gsetting.unset_proxy(pc_username)
    # bash.unset_proxy(pc_username)
    # dnf.unset_proxy()
else:
    print("Try again with correct option")

