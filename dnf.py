#!/usr/bin/python3
import os


def set_proxy(host_ip, host_port, auth_choice, pc_username, username, password ):
    check = os.path.isdir('/etc/dnf')
    if check == True :
        file_temp = open('/etc/dnf/dnf.conf_temp', 'w+')
        file_ob = open('/etc/dnf/dnf.conf', 'r')
        for line in file_ob.readlines():
            if 'proxy' in line or 'proxy_username' in line or 'proxy_password' in line: 
                continue
            else:
                file_temp.write(line)
            file_temp.write('proxy=http://' + host_ip + ':' + host_port)
            if auth_choice == 'yes':
                file_temp.write('proxy_username=' + username )
                file_temp.write('proxy_password=' + password )

            file_ob.close()
            file_temp.close()
            os.remove('/etc/dnf/dnf.conf')
            os.rename('/etc/dnf/dnf.conf_temp', '/etc/dnf/dnf.conf')

def unset_proxy():
    check = os.path.isdir('/etc/dnf')
    if check == True :
        file_temp = open('/etc/dnf/dnf.conf_temp', 'w+')
        file_ob = open('/etc/dnf/dnf.conf', 'r')
        for line in file_ob.readlines():
            if 'proxy' in line or 'proxy_username' in line or 'proxy_password' in line: 
                continue
            else:
                file_temp.write(line)
            file_ob.close()
            file_temp.close()
            os.remove('/etc/dnf/dnf.conf')
            os.rename('/etc/dnf/dnf.conf_temp', '/etc/dnf/dnf.conf')    