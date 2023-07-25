from scapy.all import srp, Ether, ARP, conf, IP, ICMP,sr1
import argparse
import os

parser = argparse.ArgumentParser(prog="python second.py",description="Verifie si les hotes sont présents sur le reseau en envoyant des paquets ARP who has")
parser.add_argument("target", help="entrez une addresse ip ou un reseau (192.168.10.0/24) à scanner")
parser.add_argument("-p","--ping",  action='store_true',help="Verifie si les hotes répondent aux ping")
parser.add_argument("-v", "--verbose", action='store_true', help="Les resultats sont plus détaillé")
parser.add_argument("-n","--nmap",action="store_true",help="scanner le reseau avec nmap")
args = parser.parse_args()

conf.verb = 0

ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=args.target), timeout=2)
l = []
for snd,rcv in ans:
    print("_" * 60)
    print(rcv.sprintf("%ARP.psrc% est joignable et a pour addresse MAC : %Ether.src%"))
    l.append(rcv.sprintf("%ARP.psrc%"))


if args.ping :
    p = sr1(IP(dst=l)/ICMP(),timeout=2)
    if p :
        r2 = "Cet hote répond aux ping"
    else :
        r2 = "cet hote ne réponds pas aux ping"
    printPing = True

if printPing :
    print("_"*60)
    print(r2)
    print("_" * 60)
else:
    print("_"*60)
    print("_" * 60)
if(args.nmap):
    os.system("nmap " + args.target)
        





