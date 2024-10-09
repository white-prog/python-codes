import socket

def FindDnsname(ip_address):
    try:
        dns_name, _, _ = socket.gethostbyaddr(ip_address)
        return dns_name
    except:
        return "Not valid IP address"

print(FindDnsname("8.8.8.8"))

ip_addresses = [
    "8.8.8.8",        # Google Public DNS
    "8.8.4.4",        # Google Public DNS
    "1.1.1.1",        # Cloudflare DNS
    "1.0.0.1",        # Cloudflare DNS
    "208.67.222.222", # OpenDNS
    "208.67.220.220", # OpenDNS
    "9.9.9.9",        # Quad9
    "149.112.112.112",# Quad9
    "127.0.0.1"
    
]

dic = {}
for i in ip_addresses:
    dic[i] = FindDnsname(i)
print("Dictionary of IP address : DNS name")
print(dic)