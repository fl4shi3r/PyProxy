#!/usr/bin/python3
import os


def set_proxy(host_ip, host_port, auth_choice, pc_username, username, password):
    check = os.path.isdir('/etc/apt')
    if check == True :
        file_temp = open('/etc/apt/apt.conf_temp', 'w+')
        if os.path.exists('/etc/apt/apt.conf'):
            file_ob = open('/etc/apt/apt.conf', 'r')
        else:
            file_ob = open('/etc/apt/apt.conf', 'w+')

        for line in file_ob.readlines():
            if 'Acquire::http::proxy' in line or 'Acquire::https::proxy' in line or 'Acquire::ftp::proxy' in line or line.isspace():
                continue    
            else:
                file_temp.write(line)
        if auth_choice == 'yes':
            file_temp.write('Acquire::http::proxy "http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '/";'+ '\n')
            file_temp.write('Acquire::https::proxy "http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '/";'+ '\n')
            file_temp.write('Acquire::ftp::proxy "ftp://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '/";' + '\n')        
        elif auth_choice == 'no':
            file_temp.write('Acquire::http::proxy "http://' + host_ip +':' +  host_port + '/";'+ '\n')
            file_temp.write('Acquire::https::proxy "http://' + host_ip + ':' + host_port + '/";'+ '\n')
            file_temp.write('Acquire::ftp::proxy "ftp://' + host_ip + ':' + host_port + '/";' + '\n')
        file_ob.close()
        file_temp.close()
        os.remove('/etc/apt/apt.conf')
        os.rename('/etc/apt/apt.conf_temp', '/etc/apt/apt.conf') 

def unset_proxy():
    check = os.path.isdir('/etc/apt')
    if check == True :
        file_temp = open('/etc/apt/apt.conf_temp', 'w+')
        file_ob = open('/etc/apt/apt.conf', 'r')
        for line in file_ob.readlines():
            if 'Acquire::http::proxy' in line or 'Acquire::https::proxy' in line or 'Acquire::ftp::proxy' in line or line.isspace():
                continue    
            else:
                file_temp.write(line)

        file_ob.close()
        file_temp.close()
        os.remove('/etc/apt/apt.conf')
        os.rename('/etc/apt/apt.conf_temp', '/etc/apt/apt.conf') 