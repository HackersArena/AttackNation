import os
import dos
import gmail
import sqlhack
import md5crack
import wpress

def main():
    os.system("color 0a")
    print_banner()
    print_options()
    opt = input("Choose an option form above: ")

    if opt == 1:
        print("\n********** SQL Hacking website *********\n")
        sqlhack.interact()
        quit()

    elif opt == 2:
        print("\n********** Cracking md5 hashes *********\n")
        md5crack.interact()
        quit()

    elif opt == 3:
        print("\n*********** Gmail Hacker wizard started ********\n")
        gmail.interact()

    elif opt == 4:
        print("\n************ Crash War-ftpd Daemon Server *********\n")
        import warftpskel
        quit()

    elif opt == 5:
        print("\n*********** Denial of Service attack  *************\n")
        dos.interact()
        quit()

    elif opt == 6:
        print("\n********** Hacking Wordpress site *************\n")
        wpress.interact()
        quit()

    os.system('color 07')

    return

def print_banner():

    print("===============================================================================")
    print("|       _______   _________   _________      ______    ______    _    ___      |")
    print("|      / ___  |  |___   ___| |___   ___|    / ___  |  |   ___|  |  | /  /      |")
    print("|     / /___| |      | |         | |       / /___| |  |  |      |  |/  /       |")
    print("|    / /----| |      | |         | |      / /----| |  |  |      |  |\  \       |")
    print("|   / /     | |      | |         | |     / /     | |  |  |___   |  | \  \      |")
    print("|  /_/      |_|      |_|         |_|    /_/      |_|  |______|  |__|  \__\     |")
    print("================================================================================")
    print("\n")
    print("ATTACK NATION: Written by Tilak Maddy. Please keep an eye for more updates\n")
    return

def print_options():
    print("\nHack fast and easily by choosing options [GOOD LUCK].\n")
    s = "1. SQL inject a website\n"
    s += "2. Crack a md5 Hash\n"
    s += "3. Hack a Gmail account\n"
    s += "4. FTP Daemon - Crash server\n"
    s += "5. Denial of Service attack network\n"
    s += "6. Hack a Wordpress website\n"
    print(s)
    return

main()