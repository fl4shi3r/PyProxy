import os 


def set_proxy(host_ip, host_port, auth_choice, pc_username, username, password):
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
            if auth_choice == 'yes':
                file_temp.write('\n[http]\n\tproxy = http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\n')
                file_temp.write('[https]\n\tproxy=http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\n' )
            elif auth_choice == 'no':
                file_temp.write('\n[http]\n\tproxy = http://' + host_ip +':' +  host_port + '\n')
                file_temp.write('[https]\n\tproxy=http://' + host_ip + ':' + host_port + '\n' )
                
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
            if auth_choice == 'yes':
                file_temp.write('\n[http]\n\tproxy = http://'+ username + ':'+ password + '@' + host_ip +':' +  host_port + '\n')
                file_temp.write('[https]\n\tproxy=http://'+ username + ':'+ password + '@' + host_ip + ':' + host_port + '\n' )
            elif auth_choice == 'no':
                file_temp.write('\n[http]\n\tproxy = http://' + host_ip +':' +  host_port + '\n')
                file_temp.write('[https]\n\tproxy=http://' + host_ip + ':' + host_port + '\n' )
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
   