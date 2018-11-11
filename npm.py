import getpass, os


def set_proxy(username, password, host_ip, host_port, pc_username):
    
    
    # proxy for root user
    
    file_temp = open('/root/.npmrc_temp','w+')
    file_ob = open('/root/.npmrc','r')
    for line in file_ob.readlines():
        if 'http-proxy' in line or 'https-proxy' in line or 'proxy' in line:
            continue    
        else:
            file_temp.write(line)
    
    file_temp.write('https-proxy=http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\n')
    file_temp.write('proxy=http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port  + '\n')        
    file_ob.close()
    file_temp.close()
    os.remove('/root/.npmrc')
    os.rename('/root/.npmrc_temp', '/root/.npmrc') 
    
    
    # proxy for other users

    file_name = '/home/'+ pc_username + '/.npmrc'
    file_temp = open(file_name + '_temp', 'w+')
    file_ob = open(file_name,'r')
    for line in file_ob.readlines():
        if 'http-proxy' in line or 'https-proxy' in line or 'proxy' in line:
            continue    
        else:
            file_temp.write(line)
    
    file_temp.write('https-proxy=http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\n')
    file_temp.write('proxy=http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port  + '\n')        
    file_ob.close()
    file_temp.close()
    os.remove(file_name)
    os.rename(file_name + '_temp', file_name)

def unset_proxy(pc_username):
    # for root user
    file_temp = open('/root/.npmrc_temp','w+')
    file_ob = open('/root/.npmrc','r')
    for line in file_ob.readlines():
        if 'http-proxy' in line or 'https-proxy' in line or 'proxy' in line:
            continue    
        else:
            file_temp.write(line)
    file_ob.close()
    file_temp.close()
    os.remove('/root/.npmrc')
    os.rename('/root/.npmrc_temp', '/root/.npmrc') 

    #for other users

    file_name = '/home/'+ pc_username + '/.npmrc'
    file_temp = open(file_name + '_temp', 'w+')
    file_ob = open(file_name,'r')
    for line in file_ob.readlines():
        if 'http-proxy' in line or 'https-proxy' in line or 'proxy' in line:
            continue    
        else:
            file_temp.write(line)
    
    file_ob.close()
    file_temp.close()
    os.remove(file_name)
    os.rename(file_name + '_temp', file_name)