import os 


def set_proxy(username, password, host_ip, host_port, pc_username):
    result = os.system('which git > /dev/null')
    if result == 0 :
        if pc_username == 'root' :
            file_name = '/root/.gitconfig'
            file_temp = open(file_name + '_temp', 'w+')
            file_ob = open(file_name, 'w+')
            for line in file_ob.readlines():
                if 'http' in line or 'https' in line or 'proxy' in line:
                    continue    
                else:
                    file_temp.write(line)

            file_temp.write('\n[http]\n\tproxy = http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\n')
            file_temp.write('[https]\n\tproxy=http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\n' )
            file_ob.close()
            file_temp.close()
            os.remove(file_name)
            os.rename(file_name +'_temp', file_name)
        else:
            file_name = '/home/'+ pc_username + '/.gitconfig'
            file_temp = open(file_name + '_temp', 'w+')
            file_ob = open(file_name, 'w+')
            for line in file_ob.readlines():
                if 'http' in line or 'https' in line or 'proxy' in line:
                    continue    
                else:
                    file_temp.write(line)

            file_temp.write('\n[http]\n\tproxy = http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\n')
            file_temp.write('[https]\n\tproxy=http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\n' )
            file_ob.close()
            file_temp.close()
            os.remove(file_name)
            os.rename(file_name +'_temp', file_name)


def unset_proxy(pc_username):
    result = os.system('which git > /dev/null')
    if result == 0 :
        if pc_username == 'root' :
            file_name = '/root/.gitconfig'
            file_temp = open(file_name + '_temp', 'w+')
            file_ob = open(file_name, 'w+')
            for line in file_ob.readlines() :
                if 'http' in line or 'https' in line or 'proxy' in line:
                    continue    
                else:
                    file_temp.write(line)

            file_ob.close()
            file_temp.close()
            os.remove(file_name)
            os.rename(file_name +'_temp', file_name)
        else:
            file_name = '/home/'+ pc_username + '/.gitconfig'
            file_temp = open(file_name + '_temp', 'w+')
            file_ob = open(file_name, 'w+')
            for line in file_ob.readlines():
                if 'http' in line or 'https' in line or 'proxy' in line:
                    continue    
                else:
                    file_temp.write(line)

            file_ob.close()
            file_temp.close()
            os.remove(file_name)
            os.rename(file_name +'_temp', file_name)
   