#!/usr/bin/python3
import os

def set_proxy(host_ip, host_port, auth_choice, pc_username,  username, password):
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy mode "manual"\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http host ' + host_ip + '\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http port ' + host_port + '\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.https host ' + host_ip + '\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.https port ' + host_port + '\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.ftp host ' + host_ip + '\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.ftp port ' + host_port + '\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.socks host ' + host_ip + '\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.socks port ' + host_port + '\'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http enabled true \'' )
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http use-authentication true \'' )
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http authentication-user "' + username + '"\'' )
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http authentication-password "' + password + '"\'')



def unset_proxy(pc_username):
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy mode "none" \' ')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http host "" \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http port 0 \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.https host "" \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.https port 0 \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.ftp host "" \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.ftp port 0 \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.socks host "" \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.socks port 0 \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http enabled false \' ' )
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http use-authentication false \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http authentication-user "" \'')
    os.system('su ' + pc_username +  ' -c \'gsettings set org.gnome.system.proxy.http authentication-password "" \'')

