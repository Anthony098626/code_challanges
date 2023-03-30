#!/user/bin/env python3

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/29/2023
# Creates: a script that add's said person to AD

# Define the user's properties
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$userPrincipalName = "ferdi@GlobeXpower.com"
$office = "Springfield"
$state = "OR"
$department = "TPS Department"
$company = "GlobeX USA"
$title = "TPS Reporting Lead"

# Create a secure password for the user
$password = ConvertTo-SecureString "P@ssw0rd123" -AsPlainText -Force

# Set the AD path for the user
$ou = "OU=Users,OU=$office,OU=$state,DC=example,DC=com"

# Create the user account
New-ADUser `
    -Name $displayName `
    -GivenName $firstName `
    -Surname $lastName `
    -UserPrincipalName $userPrincipalName `
    -AccountPassword $password `
    -Enabled $true `
    -Office $office `
    -State $state `
    -Department $department `
    -Company $company `
    -Title $title `
    -Path $ou

#source: https://chat.openai.com/chat