import os


def set_proxy(username, password, host_ip, host_port):
    file_temp = open('/etc/enviromnent_temp', 'w+')
    file_ob = open('/etc/environment', 'r')
    for line in file_ob.readlines():
        if 'http_proxy' in line or 'https_proxy' in line or 'ftp_proxy' in line or line.isspace():
            continue    
        else:
            file_temp.write(line)

    file_temp.write("\n" + 'http_proxy=\'http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\''+ '\n')
    file_temp.write('https_proxy=\'http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\''+ '\n')
    file_temp.write('ftp_proxy=\'ftp://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\'' + '\n')        
    file_ob.close()
    file_temp.close()
    os.remove('/etc/environment')
    os.rename('/etc/enviromnent_temp', '/etc/environment') 

def unset_proxy():
    file_temp = open('/etc/enviromnent_temp', 'w+')
    file_ob = open('/etc/environment', 'r')
    for line in file_ob.readlines():
        if 'http_proxy' in line or 'https_proxy' in line or 'ftp_proxy' in line or line.isspace():
            continue    
        else:
            file_temp.write(line)

    file_ob.close()
    file_temp.close()
    os.remove('/etc/environment')
    os.rename('/etc/enviromnent_temp', '/etc/environment') 
   
