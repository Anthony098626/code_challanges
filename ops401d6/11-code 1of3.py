#!/user/bin/python3
import random
from scapy.all import *

# define the host IP and port range
host = "192.168.1.11"
start_port = 1
end_port = 100

# start the scan
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
# source: https://chat.openai.com/