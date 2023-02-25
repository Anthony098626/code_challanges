# Script Name:12-code.sh                
# Class Name:Ops 201
# Author Name:Anthony Wall
# Date of latest revision:02/24/2023      
# Purpose: Powershell Script returning IPv4 

# Main 


Get-NetIPAddress -AddressFamily IPv4 | Select-Object -ExpandProperty IPAddress

$ipconfig = ipconfig /all
$ipv4 = $ipconfig | Select-String -Pattern '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | Select-Object -ExpandProperty Matches | Select-Object -ExpandProperty Value
Write-Host "IPv4 address: $ipv4"

#End 

Sourced from chatgbt.com 