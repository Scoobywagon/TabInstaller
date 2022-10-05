import urllib.request
import platform
import sys

#Set up the environment
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

baseurl = "https://downloads.tableau.com/esdalt/"

os_platform = platform.platform()
os_platform = 'Linux-3.10.0-1160.el7.x86_64-x86_64-with-centos-7.9.2009-Core'

#get options from the user.
version = input("What version would you like to install (ex. 2022.1.6)?  ")
tabcmd = input("Get TABCMD as well (y/n)?")

#format filenames and URLs
installer = version.replace(".","-")

if "Windows" in os_platform:
    print(bcolors.OKBLUE,"Platform is \033[1mWindows \033[0m")
    server_installer = "TableauServer-64bit-" + installer + ".exe"
    tabcmd_installer = "TableauServerTabcmd-64bit-" + installer + ".exe"
    desktop_installer = "TableauDesktop-64bit-" + installer + ".exe"
elif "centos" in os_platform:
    print(bcolors.OKGREEN, "Platform is \033[1mCentos\033[0m")
    server_installer = "tableau-server-" + installer + "_amd64.deb"
    tabcmd_installer = "tableau-tabcmd-" + installer + "_all.deb"
else:
    print(bcolors.OKGREEN, "Platform is Linux")
    server_installer = "tableau-server-" + installer + ".x86_64.rpm"
    tabcmd_installer = "tableau-tabcmd-" + installer + ".noarch.rpm"

server_target_url = baseurl + version + "/" + server_installer
tabcmd_target_url = baseurl + version + "/" + tabcmd_installer

#begin downloads
print("Downloading " + server_installer)
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
