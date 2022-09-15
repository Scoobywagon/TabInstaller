$baseurl = "https://downloads.tableau.com/esdalt/"
$localpath = "$home\Downloads" #Edit this if you want your download to land somewhere other than the default downloads folder
$desktop = [Environment]::GetFolderPath("Desktop")
$atr = $null

$install_log = $desktop + "\TableauServerInstall.Log"  #Edit this if you want the Tableau Server install log to land somewhere other than the desktop.
$install_args = "/install " + "/quiet " + "/norestart " + "/log `"" + $install_log + "`""

$version = Read-Host -Prompt "Please specify the full version (ex. 2022.1.6) of Tableau Server you would like to install. "
If ($version -like "20??.[0-9].[0-9]") {

} else {
    Write-host "This does not appear to be a valid version.  Please try again."
    exit
}

$atr = Read-Host -Prompt "Use Authorization-To-Run for Tableau Server?"

If (($atr -eq "y") -OR ($atr -eq "Y")) {
    Write-Host "Using ATR for Server Activation."
    $install_args = $install_args + " ACTIVATIONSERVICE=`"1`""
} else {
    Write-Host "Ignoring ATR."
    $install_args = $install_args + " ACTIVATIONSERVICE=`"0`""
}


$installer = $version.Replace(".","-")
$installer = "TableauServer-64bit-" + $installer + ".exe"

$targeturl = $baseurl + $version + "/" + $installer
$filedownload = $localpath + "\" + $installer

Write-Host "Retrieving $installer from $targeturl"

If (Test-Path $filedownload) { 
    Write-Host "$installer already exists.  Skipping download."
} else {
    Invoke-WebRequest -Uri $targeturl -OutFile $filedownload
    Write-Host "Done."
}

Invoke-Expression "explorer '/select,$filedownload'"

Write-Host "This script will now install Tableau Server version $version in the default location"

Invoke-Expression "$filedownload $install_args"
