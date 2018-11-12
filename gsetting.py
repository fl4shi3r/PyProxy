import os

def set_proxy(username, password, host_ip, host_port, pc_username):
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy mode "manual"')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http host ' + host_ip)
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http port ' + host_port)
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.https host ' + host_ip)
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.https port ' + host_port)
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.ftp host ' + host_ip)
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.ftp port ' + host_port)
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http authentication-user ' + username )
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http authentication-password ' + password)


def unset_proxy(pc_username):
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy mode "none" ')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http host ""')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http port 0')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.https host ""')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.https port 0')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.ftp host ""')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.ftp port 0')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http use-authentication false')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http authentication-user ""')
    os.system('sudo -u ' + pc_username + ' gsettings set org.gnome.system.proxy.http authentication-password ""')