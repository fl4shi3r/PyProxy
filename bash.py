import os


def set_proxy(username, password, host_ip, host_port, pc_username):
    if pc_username == 'root':
        file_name = '/root/.bashrc'
        file_temp = open(file_name + '_temp', 'w+')
        file_ob = open(file_name, 'r')

        for line in file_ob.readlines():
            if 'http_proxy' in line or 'https_proxy' in line or 'ftp_proxy' in line:
                continue    
            else:
                file_temp.write(line)

        file_temp.write("\n" + 'http_proxy=\'http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\''+ '\n')
        file_temp.write('https_proxy=\'http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\''+ '\n')
        file_temp.write('ftp_proxy=\'ftp://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\'' + '\n')        
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

        file_temp.write("\n" + 'http_proxy=\'http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\''+ '\n')
        file_temp.write('https_proxy=\'http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\''+ '\n')
        file_temp.write('ftp_proxy=\'ftp://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\'' + '\n')        
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