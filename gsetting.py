#!/usr/bin/python3
import os

def set_proxy(host_ip, host_port, auth_choice, pc_username,  username, password):
    os.system('  gsettings set org.gnome.system.proxy mode "manual"')
    os.system('  gsettings set org.gnome.system.proxy.http host ' + host_ip)
    os.system('  gsettings set org.gnome.system.proxy.http port ' + host_port)
    os.system('  gsettings set org.gnome.system.proxy.https host ' + host_ip)
    os.system('  gsettings set org.gnome.system.proxy.https port ' + host_port)
    os.system('  gsettings set org.gnome.system.proxy.ftp host ' + host_ip)
    os.system('  gsettings set org.gnome.system.proxy.ftp port ' + host_port)
    os.system('  gsettings set org.gnome.system.proxy.http enabled true' )
    os.system('  gsettings set org.gnome.system.proxy.http use-authentication true' )
    os.system('  gsettings set org.gnome.system.proxy.http authentication-user "' + username + '"' )
    os.system('  gsettings set org.gnome.system.proxy.http authentication-password "' + password + '"')



def unset_proxy(pc_username):
    os.system('  gsettings set org.gnome.system.proxy mode "none" ')
    os.system('  gsettings set org.gnome.system.proxy.http host ""')
    os.system('  gsettings set org.gnome.system.proxy.http port 0')
    os.system('  gsettings set org.gnome.system.proxy.https host ""')
    os.system('  gsettings set org.gnome.system.proxy.https port 0')
    os.system('  gsettings set org.gnome.system.proxy.ftp host ""')
    os.system('  gsettings set org.gnome.system.proxy.ftp port 0')
    os.system('  gsettings set org.gnome.system.proxy.http enabled false' )
    os.system('  gsettings set org.gnome.system.proxy.http use-authentication false')
    os.system('  gsettings set org.gnome.system.proxy.http authentication-user ""')
    os.system('  gsettings set org.gnome.system.proxy.http authentication-password ""')

