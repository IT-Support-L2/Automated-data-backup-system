# PowerShell script for initiating the backup process

# Define variables
$sourceDirectory = "C:\Path\To\Source\Directory"
$destinationDirectory = "D:\Path\To\Backup\Directory"
$logFile = "C:\Path\To\Log\backup_log.txt"

# Log start of backup process
Add-Content -Path $logFile -Value "$(Get-Date): Backup process initiated."

# Execute Python script for backup
python.exe .\backup_script.py $sourceDirectory $destinationDirectory >> $logFile 2>&1

# Log end of backup process
Add-Content -Path $logFile -Value "$(Get-Date): Backup process completed."