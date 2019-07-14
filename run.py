import re, os, getpass, sys
import environment, apt, npm, git, gsetting, bash, dnf #Local Python files


def password_hex(password):
    hex_password = []
    for i in password:
        if i in ['@','!','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}',';',':','"',"'",',','<','.','>','/','?','`','~',' ']:
            hex_password.append('%' + str(hex(ord(i))[2:]))
        else:
            hex_password.append(i)
    return ''.join(hex_password)

def run_set(host_ip, host_port, pc_username, auth_choice, username, password):
    environment.set_proxy(host_ip, host_port, auth_choice, pc_username, username, password)
    apt.set_proxy(host_ip, host_port, auth_choice,pc_username, username, password)
    npm.set_proxy( host_ip, host_port, auth_choice,pc_username, username, password)
    git.set_proxy(host_ip, host_port, auth_choice, pc_username,username, password )
    gsetting.set_proxy(host_ip, host_port, auth_choice,pc_username, username, password)
    bash.set_proxy(host_ip, host_port, auth_choice,pc_username, username, password)
    dnf.set_proxy(host_ip, host_port, auth_choice,pc_username, username, password)

def saved(save_dir):
    file = 'Saved/' + save_dir[0]
    f = open(file, 'r')
    x = f.readlines()
    host_ip = x[0][:-1]
    host_port = x[1][:-1]
    pc_username = x[2][:-1]
    if(len(x) > 3):
        username = x[3][:-1]
        password = x[4][:-1]
        auth_choice = 'yes'
    else:
        username = ''
        password = ''
        auth_choice = 'no'
    run_set(host_ip, host_port, pc_username, auth_choice, username, password)

def unsaved():
    file = 'Saved/proxy.txt'
    fun = open(file, 'w')
    host_ip = input('Enter the Proxy Host address: ')
    host_port = input('Enter the Proxy host port: ')
    pc_username = input('Enter the pc username: ')

    if (os.path.isdir('/home/'+pc_username) or pc_username == 'root'):
        username = ''
        password = ''
        auth_choice = (input('Is authentication required in your college/organization (yes/no): ')).lower()
        if auth_choice == 'yes' :
            username = input('Enter the username: ')
            password_unhexed = getpass.getpass(prompt='Enter the password: ')
            password = password_hex(password_unhexed)
        elif auth_choice == 'no':
            pass
        else:
            print('Try again with correct option')
            exit(1)
        fun.write(host_ip + '\n')
        fun.write(host_port + '\n')
        fun.write(pc_username + '\n')
        fun.write(username + '\n')
        fun.write(password + '\n')

    run_set(host_ip, host_port, pc_username, auth_choice, username, password)

def set_proxy():
    save_dir = os.listdir('Saved')
    if len(save_dir) == 0:
        file = 'Saved/proxy.txt'
        fun = open(file, 'w')
    save_dir = os.listdir('Saved')
    file = 'Saved/' + save_dir[0]
    f = open(file, 'r')
    x = f.readlines()
    if(len(x) > 0):
        print('There is proxy saved of IP ' + x[0][:-1] + ' and username ' + x[3][:-1])
        file_use = input('do you wanna use that??(y/n)')
        if(file_use == 'y'):
            saved(save_dir)
        else:
            unsaved()
    else:
        unsaved()
    print('set')

def unset_proxy():
    file = 'Saved/proxy.txt'
    f = open(file, 'r')
    x = f.readlines()
    pc_username = x[2][:-1]
    print(pc_username)
    if (os.path.isdir('/home/'+pc_username) or pc_username == 'root'):
        environment.unset_proxy()
        apt.unset_proxy()
        npm.unset_proxy(pc_username)
        git.unset_proxy(pc_username)
        # gsetting.unset_proxy(pc_username)
        bash.unset_proxy(pc_username)
        dnf.unset_proxy()
        os.system("su -c \"echo 3 >'/proc/sys/vm/drop_caches' && swapoff -a && swapon -a\"")
        # reboot_choice = (input('Reboot is required to apply the changes\nDo you want to reboot your system(yes/no)')).lower()
        # if reboot_choice == "yes":
        #     print('Rebooting your system')
        #     os.system('reboot')

    else:
        print("Incorrect pc username. Try again with correct pc username")
        exit(1)


def start():
    choice = int(input('1.set proxy\n2.unset proxy\nEnter your choice (1/2): '))
    if choice == 1:
        set_proxy()
    elif choice == 2:
        unset_proxy()
    else:
        print('Wrong Input')



if __name__ == '__main__':
    if sys.version_info.major < 3:
        print('Kindly use python3 to run this scrypt')
    else:
        if os.geteuid() != 0:
            exit('You need root privileges to run this script.\nPlease try again, this time using "sudo".\nExiting.')
        else:
            start()
