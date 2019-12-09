# script captures to a .pcap file for a finite packet count or timeout
# then sniffs for pkt.len and plots the graph
# main() loops the functions infinitely 
# .pcap file gets overwritten each iteration

from scapy.all import *
import matplotlib.pyplot as plt
import mpld3

# packet capture to .pcap file 
def capPkt ():

    cap = sniff(iface='Ethernet 4',count=20)
    wrpcap('pktcap.pcap', cap)


# create graph from .pcap with packet length as the y-axis
def capSniff ():

    plt.ylabel("Bytes")
    plt.xlabel("Packet Count")
    plt.title("Real Time Packet Length")

    pktBytes=[]

    for pkt in sniff(offline='pktcap.pcap'): 
        if IP in pkt:
            try:
                pktBytes.append(pkt[IP].len)
                plt.plot(pktBytes)
                plt.pause(1.0)
                plt.clf() #clear axis after packet count or timeout reached for next iteration
 
            except KeyboardInterrupt:
                quit()

    
                

# loops functions in order to keep capture file finite to save on resources
def main ():

    while True:

        capPkt()
        capSniff()


if __name__ == '__main__': main()