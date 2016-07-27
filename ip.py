import socket

def get_ip(url):
    ipaddr = socket.gethostbyname(url)
    return ipaddr

def get_name(ip):
    name = socket.gethostbyaddr(ip)
    return name

