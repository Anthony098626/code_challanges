#!/user/bin/python3
import ipaddress
import random
import subprocess
from scapy.all import *

def scan_port(host, port):
    src_port = random.randint(1025,65534) # choose a random source port
    response = sr1(IP(dst=host)/TCP(sport=src_port,dport=port,flags="S"),timeout=1,verbose=0) # send a TCP SYN packet
    if response is None: # no response
        return f"Port {port} is filtered (silently dropped)"
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12: # 0x12 --> SYN-ACK, port is open
        send(IP(dst=host)/TCP(sport=src_port,dport=port,flags="R"),verbose=0) # send a RST packet
        return f"Port {port} is open"
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14: # 0x14 --> RST-ACK, port is closed
        return f"Port {port} is closed"


# Allow the user to specify a range of IPs and have the tool scan each one in succession
while True:
    try:
        target = input("Please enter a comma-separated list of IP addresses or ranges: ")
        targets = target.split(",")
        target_hosts = set()
        for t in targets:
            if "/" in t:
                target_hosts |= set(str(host) for host in ipaddress.ip_network(t, strict=False).hosts())
            else:
                target_hosts.add(t.strip())
        if not target_hosts:
            raise ValueError
    except ValueError:
        print("Invalid target. Please try again.")
        continue
    else:
        break

# Combine the two modes of your network scanner script
for host in target_hosts:
    response = subprocess.run(['ping', '-c', '1', '-W', '1', host], stdout=subprocess.DEVNULL)
    if response.returncode == 0:
        icmp_type = ICMP().type
        icmp_code = ICMP().code
        if icmp_type == 3 and icmp_code in [1,2,3,9,10,13]:
            print(f"{host} is blocking ICMP traffic")
        else:
            print(f"{host} is responding")
            for port in range(1, 1025):
                result = scan_port(host, port)
                if result:
                    print(result)
    else:
        print(f"{host} is down/unresponsive")
# source: chat gbt