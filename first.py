# © ALL RIGHTS OWNED TO https://github.com/drexBaxesse ©

import socket

BANNER = r"""
***********************************************************************************
    __        _______ _     ____ ___  __  __ _____   _____ ___    __  ____   __
\ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \  |  \/  \ \ / /
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | | | |\/| |\ V / 
  \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| | | |  | | | |  
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/  |_|  |_| |_|  
                                                                           
 ____ ___ _____ _____   _____ ___    ___ ____  
/ ___|_ _|_   _| ____| |_   _/ _ \  |_ _|  _ \ 
\___ \| |  | | |  _|     | || | | |  | || |_) |
 ___) | |  | | | |___    | || |_| |  | ||  __/ 
|____/___| |_| |_____|   |_| \___/  |___|_|    
                                               
    _    ____  ____  ____  _____ ____ ____  
   / \  |  _ \|  _ \|  _ \| ____/ ___/ ___| 
  / _ \ | | | | | | | |_) |  _| \___ \___ \ 
 / ___ \| |_| | |_| |  _ <| |___ ___) |__) |
/_/   \_\____/|____/|_| \_\_____|____/____/ 
                                            
 ____  ____   ___   ____ ____      _    __  __ 
|  _ \|  _ \ / _ \ / ___|  _ \    / \  |  \/  |
| |_) | |_) | | | | |  _| |_) |  / _ \ | |\/| |
|  __/|  _ <| |_| | |_| |  _ <  / ___ \| |  | |
|_|   |_| \_\\___/ \____|_| \_\/_/   \_\_|  |_|

© OWNER SCRIPTER: "https://github.com/drexBaxesse"

***********************************************************************************

    """


def main():
    print(BANNER)
    site = input("Enter a hostname (for example, example.com): ").strip()
    if not site:
        print("[ERROR] Please enter a hostname.")
        return

    try:
        ip_address = socket.gethostbyname(site)
    except socket.gaierror:
        print(f"[ERROR] Could not resolve '{site}'. Check the hostname and your network connection.")
        return

    site_host = socket.gethostname()
    print(f"[IP ADDRESS]: {ip_address}")
    print(f"home host: {site_host}")
    print(f"{site} [{ip_address}] --> {site_host}")


if __name__ == "__main__":
    main()
