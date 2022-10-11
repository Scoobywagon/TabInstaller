from http import server
from os import getcwd
import urllib.request
import platform
import os.path
import subprocess

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
install_args = "/install /quiet /norestart /log \"TableauServerInstall.log\""
os_platform = platform.platform()
#os_platform = 'Linux-3.10.0-1160.el7.x86_64-x86_64-with-centos-7.9.2009-Core'
current_dir = getcwd()

#get options from the user.
print(bcolors.HEADER)
print("This script will download and install Tableau Server for you.")
print("Optionally, it will also download Tableau Desktop and TABCMD in the same version.")
print("If you elect to download Tableau Desktop, this script will grab both Windows and Mac versions.")
print("All installers will land in ", current_dir)
print(bcolors.ENDC)
version = input("What version would you like to install (ex. 2022.1.6)?  ")
tabcmd = input("Get TABCMD as well (y/n)?")
desktop = input("Get Tableau Desktop (y/n)?")

#format filenames and URLs
installer = version.replace(".","-")

if "Windows" in os_platform:
    print(bcolors.OKBLUE,"Platform is \033[1mWindows \033[0m",bcolors.ENDC)
    operating_system = "windows"
    server_installer = "TableauServer-64bit-" + installer + ".exe"
    tabcmd_installer = "TableauServerTabcmd-64bit-" + installer + ".exe"
    win_desktop_installer = "TableauDesktop-64bit-" + installer + ".exe"
    mac_desktop_installer = "TableauDesktop-" + installer + ".dmg"
elif "centos" in os_platform:
    print(bcolors.OKGREEN, "Platform is \033[1mCentos\033[0m",bcolors.ENDC)
    operating_system = "debian"
    server_installer = "tableau-server-" + installer + "_amd64.deb"
    tabcmd_installer = "tableau-tabcmd-" + installer + "_all.deb"
    win_desktop_installer = "TableauDesktop-64bit-" + installer + ".exe"
    mac_desktop_installer = "TableauDesktop-" + installer + ".dmg"
else:
    print(bcolors.OKGREEN, "Platform is Linux",bcolors.ENDC)
    operating_system = "rhel"
    server_installer = "tableau-server-" + installer + ".x86_64.rpm"
    tabcmd_installer = "tableau-tabcmd-" + installer + ".noarch.rpm"
    win_desktop_installer = "TableauDesktop-64bit-" + installer + ".exe"
    mac_desktop_installer = "TableauDesktop-" + installer + ".dmg"

server_target_url = baseurl + version + "/" + server_installer
tabcmd_target_url = baseurl + version + "/" + tabcmd_installer
win_desktop_target_url = baseurl + version + "/" + win_desktop_installer
mac_desktop_target_url = baseurl + version + "/" + mac_desktop_installer

#check if we've already downloaded the installer(s).  If not, download them.
if not os.path.isfile(server_installer):
    #begin downloads
    print("Downloading " + server_installer)
    with urllib.request.urlopen(server_target_url) as response, open(server_installer, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
else:
    print(bcolors.OKCYAN,"Server installer is already here.",bcolors.ENDC)


if tabcmd == 'y':
    if not os.path.isfile(tabcmd_installer):
        print("Downloading " + tabcmd_installer)
        with urllib.request.urlopen(tabcmd_target_url) as response, open(tabcmd_installer, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    else:
        print(bcolors.OKCYAN,"TABCMD installer is already here.",bcolors.ENDC)


if desktop == 'y':
    if not os.path.isfile(win_desktop_installer):
        print("Downloading " + win_desktop_installer)
        with urllib.request.urlopen(win_desktop_target_url) as response, open(win_desktop_installer, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    else:
        print(bcolors.OKCYAN,"Windows Desktop installer is already here.",bcolors.ENDC)

    if not os.path.isfile(mac_desktop_installer):
        print("Downloading " + mac_desktop_installer)
        with urllib.request.urlopen(mac_desktop_target_url) as response, open(mac_desktop_installer, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    else:
        print(bcolors.OKCYAN,"Mac Desktop installer is alredy here.",bcolors.ENDC)

if operating_system == "windows":
    installer_args = "./" + server_installer + " /install /norestart /log \"serverinstall.log\""

    print(installer_args)
    #subprocess.run(server_installer, "/install " + "/quiet " + "/norestart " + "/log  \"serverinstall.log\"")
    subprocess.run(installer_args)

elif operating_system == "debian":
    print("Installing for Debian-like OS.")

elif operating_system == "rhel":
    print("Installing for RHEL OS.")

else:
    print("Platform is indeterminate.  Unable to continue installing.")
    exit()
