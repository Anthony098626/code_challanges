# Script Name:12-code.sh                
# Class Name:Ops 201
# Author Name:Anthony Wall
# Date of latest revision:02/21/2023      
# Purpose: 

#Main 

Enable File and Printer Sharing
Set-NetFirewallRule -DisplayGroup "File and Printer Sharing" -Enabled True

Allow ICMP traffic
New-NetFirewallRule -DisplayName "Allow ICMPv4-In" -Protocol ICMPv4 -IcmpType 8 -Enabled True

Enable Remote management
Enable-PSRemoting -Force

Remove bloatware
Get-MpThreatCatalog | Where-Object {$_.Name -like "Malware Signature"} | Remove-MpThreatCatalogEntry

Enable Hyper-V
Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart

Disable SMBv1, an insecure protocol
Set-SmbServerConfiguration -EnableSMB1Protocol $false


# End 