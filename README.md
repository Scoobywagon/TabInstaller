# TabInstaller
Automated download/install of Tableau Server
When you run this powershell script, it will ask you what version of Tableau Server you want to install, and whether you want to use ATR or not.  It will then do some (minor) input validation.  If that passes, it will check if your requested installer already exists in your Downloads folder.  If so, it will run the installer with an appropriate set of flags.  If not, it will try to download the installer and then run it with the appropriate flags.

Error checking is nearly non-existent, so play nice.
