from scapy.layers.l2 import ARP, Ether
from scapy.all import srp

def scan(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    results = []

    for element in answered_list:
        result = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        results.append(result)

    return results

def display_results(results):
    print("IP Address\t\tMAC Address")
    print("--------------------------------------")
    for result in results:
        print(result["ip"] + "\t\t" + result["mac"])


target_ip = "192.168.0.1/24"
scan_results = scan(target_ip)
display_results(scan_results)