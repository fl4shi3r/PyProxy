#!/usr/bin/python3
import os


def set_proxy(host_ip, host_port, auth_choice, pc_username, username, password):
    if pc_username == 'root':
        file_name = '/root/.bashrc'
        file_temp = open(file_name + '_temp', 'w+')
        file_ob = open(file_name, 'r')

        for line in file_ob.readlines():
            if 'http_proxy' in line or 'https_proxy' in line or 'ftp_proxy' in line:
                continue    
            else:
                file_temp.write(line)
        if auth_choice == 'yes':
            file_temp.write("\n" + 'http_proxy=\'http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\''+ '\n')
            file_temp.write('https_proxy=\'http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\''+ '\n')
            file_temp.write('ftp_proxy=\'ftp://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\'' + '\n')        
        elif auth_choice == 'no':
            file_temp.write("\n" + 'http_proxy=\'http://' + host_ip +':' +  host_port + '\''+ '\n')
            file_temp.write('https_proxy=\'http://' + host_ip + ':' + host_port + '\''+ '\n')
            file_temp.write('ftp_proxy=\'ftp://' + host_ip + ':' + host_port + '\'' + '\n') 
        file_ob.close()
        file_temp.close()
        os.remove(file_name)
        os.rename(file_name + '_temp', file_name) 
    else:
        file_name = '/home/'+ pc_username + '/.bashrc'
        file_temp = open(file_name + '_temp', 'w+')
        file_ob = open(file_name, 'r')
        for line in file_ob.readlines():
            if 'http_proxy' in line or 'https_proxy' in line or 'ftp_proxy' in line:
                continue    
            else:
                file_temp.write(line)
        if auth_choice == 'yes':
            file_temp.write("\n" + 'http_proxy=\'http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\''+ '\n')
            file_temp.write('https_proxy=\'http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\''+ '\n')
            file_temp.write('ftp_proxy=\'ftp://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\'' + '\n')        
        elif auth_choice == 'no':
            file_temp.write("\n" + 'http_proxy=\'http://' + host_ip +':' +  host_port + '\''+ '\n')
            file_temp.write('https_proxy=\'http://' + host_ip + ':' + host_port + '\''+ '\n')
            file_temp.write('ftp_proxy=\'ftp://' + host_ip + ':' + host_port + '\'' + '\n')
        file_ob.close()
        file_temp.close()
        os.remove(file_name)
        os.rename(file_name + '_temp', file_name) 

def unset_proxy(pc_username):
    if pc_username == 'root':
        file_name = '/root/.bashrc'
        file_temp = open(file_name + '_temp', 'w+')
        file_ob = open(file_name, 'r')
        for line in file_ob.readlines():
            if 'http_proxy' in line or 'https_proxy' in line or 'ftp_proxy' in line:
                continue    
            else:
                file_temp.write(line)

        file_ob.close()
        file_temp.close()
        os.remove(file_name)
        os.rename(file_name + '_temp', file_name) 
    else:   
        file_name = '/home/'+ pc_username + '/.bashrc'
        file_temp = open(file_name + '_temp', 'w+')
        file_ob = open(file_name, 'r')
        for line in file_ob.readlines():
            if 'http_proxy' in line or 'https_proxy' in line or 'ftp_proxy' in line:
                continue    
            else:
                file_temp.write(line)

        file_ob.close()
        file_temp.close()
        os.remove(file_name)
        os.rename(file_name + '_temp', file_name) 