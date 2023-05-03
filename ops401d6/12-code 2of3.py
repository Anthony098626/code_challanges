#!/user/bin/python3
import ipaddress
import random
import subprocess
import sys
from scapy.all import *

# Define the menu for user choice
print("Welcome to the Network Security Tool:")
print("[1] TCP Port Range Scanner mode")
print("[2] ICMP Ping Sweep mode")

while True:
    try:
        user_choice = int(input("Please enter your choice (1 or 2): "))
        if user_choice not in [1,2]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please choose 1 or 2.")
        continue
    else:
        break

if user_choice == 1:
    # TCP port range scanner mode
    # Define the host IP and port range
    host = input("Please enter the host IP address: ")
    start_port = int(input("Please enter the start port of the range: "))
    end_port = int(input("Please enter the end port of the range: "))
    
    # Start the scan
    for port in range(start_port, end_port+1):
        src_port = random.randint(1025,65534) # choose a random source port
        response = sr1(IP(dst=host)/TCP(sport=src_port,dport=port,flags="S"),timeout=1,verbose=0) # send a TCP SYN packet
        if response is None: # no response
            print("Port",port,"is filtered (silently dropped)")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12: # 0x12 --> SYN-ACK, port is open
            send(IP(dst=host)/TCP(sport=src_port,dport=port,flags="R"),verbose=0) # send a RST packet
            print("Port",port,"is open")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14: # 0x14 --> RST-ACK, port is closed
            print("Port",port,"is closed")

elif user_choice == 2:
    # ICMP ping sweep mode
    # Prompt the user for the network address
    while True:
        try:
            network_address = ipaddress.ip_network(input("Please enter the network address (e.g. 10.10.0.0/24): "), strict=False)
        except ValueError:
            print("Invalid network address. Please try again.")
            continue
        else:
            break
    
    # Create a list of all addresses in the given network
    hosts_list = [str(host) for host in network_address.hosts()]
    
    # Ping all hosts on the network except for network address and broadcast address
    alive_hosts = []
    for host in hosts_list:
        if host == str(network_address.network_address) or host == str(network_address.broadcast_address):
            continue
        response = subprocess.run(['ping', '-c', '1', '-W', '1', host], stdout=subprocess.DEVNULL)
        if response.returncode == 0:
            icmp_type = ICMP().type
            icmp_code = ICMP().code
            if icmp_type == 3 and icmp_code in [1,2,3,9,10,13]:
                print(host, "is blocking ICMP traffic")
            else:
                print(host, "is responding")
                alive_hosts.append(host)
        else:
            print(host, "is down/unresponsive")
    
    # Count how many hosts are online and inform the user
    print("Scan complete. Found", len(alive_hosts), "hosts online:", alive_hosts)

# source: https://chat.openai.com/