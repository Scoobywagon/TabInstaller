import urllib.request
import platform
import sys


baseurl = "https://downloads.tableau.com/esdalt/"
os_platform = platform.platform()
#os_platform = 'Linux-3.10.0-1160.el7.x86_64-x86_64-with-centos-7.9.2009-Core'

version = input("What version would you like to install?  ")
installer = version.replace(".","-")

tabcmd = input("Get TABCMD as well (y/n)?")

if "Windows" in os_platform:
    print("Platform is Windows")
    server_installer = "TableauServer-64bit-" + installer + ".exe"
    tabcmd_installer = "TableauServerTabcmd-64bit-" + installer + ".exe"
    desktop_installer = "TableauDesktop-64bit-" + installer + ".exe"
elif "centos" in os_platform:
    print("Platform is Centos")
    server_installer = "tableau-server-" + installer + "_amd64.deb"
    tabcmd_installer = "tableau-tabcmd-" + installer + "_all.deb"
else:
    print("Platform is Linux")
    server_installer = "tableau-server-" + installer + ".x86_64.rpm"
    tabcmd_installer = "tableau-tabcmd-" + installer + ".noarch.rpm"

server_target_url = baseurl + version + "/" + server_installer
tabcmd_target_url = baseurl + version + "/" + tabcmd_installer

print("Downloading " + server_target_url)
with urllib.request.urlopen(server_target_url) as response, open(server_installer, 'wb') as out_file:
    data = response.read()
    out_file.write(data)

if tabcmd == 'y':

    print("Downloading " + tabcmd_installer)
    with urllib.request.urlopen(tabcmd_target_url) as response, open(tabcmd_installer, 'wb') as out_file:
        data = response.read()
        out_file.write(data)

if desktop_installer:
    print("Downloading " + desktop_installer)
    desktop_target_url = baseurl + version + "/" + desktop_installer
    with urllib.request.urlopen(desktop_target_url) as response, open(desktop_installer, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
