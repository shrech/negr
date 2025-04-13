import os
import time
from colorama import Fore, init
from pystyle import Colorate, Colors
import requests

init(autoreset=True)

WEBHOOK_URL = "https://discord.com/api/webhooks/TON_WEBHOOK_ICI"

def send_to_webhook(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except Exception as e:
        print(Fore.RED + f"[Erreur Webhook] {e}")

def execute_script(option_num):
    script_name = f"input/{str(option_num)}.py"  # Recherche dans le dossier 'input'
    if os.path.exists(script_name):
        os.system(f"python {script_name}")  # Exécute le script
    else:
        print(Fore.RED + f"[!] Le script {script_name} est introuvable.")
        time.sleep(2)

def show_banner():
    banner = r'''
                              ███▄    █ ▓█████   ▄████ ▓█████  ██▀███
                              ██ ▀█   █ ▓█   ▀  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                             ▓██  ▀█ ██▒▒███   ▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                             ▓██▒  ▐▌██▒▒▓█  ▄ ░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄
                             ▒██░   ▓██░░▒████▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
                             ░ ▒░   ▒ ▒ ░░ ▒░ ░ ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                             ░ ░░   ░ ▒░ ░ ░  ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
                            ░   ░ ░    ░   ░ ░   ░    ░     ░░
                             ░    ░  ░      ░    ░  ░   ░

                                       By   A L E X x13
'''
    print(Colorate.Vertical(Colors.rainbow, banner))

def show_tool_table():
    table = '''
┌──────────────────────────────┬──────────────────────────────┬──────────────────────────────┬──────────────────────────────┐
│          Option #1           │          Option #2           │          Option #3           │          Option #4           │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ [01] > Token Checker         │ [05] > Webhook Spammer       │ [09] > Avatar Grabber        │ [13] > Discord Status Checker│
│ [02] > Token Permissions     │ [06] > Webhook Destroyer     │ [10] > Banner Grabber        │ [14] > IP Lookup             │
│ [03] > DM Spammer            │ [07] > Nitro Generator       │ [11] > Token Logger Gen      │ [15] > IP Info Perso         │
│ [04] > Message Spammer       │ [08] > Username Checker      │ [12] > Mass Report Tool      │ [16] > Reverse DNS Lookup    │
│ [17] > Port Scanner          │ [21] > Subdomain Finder      │ [25] > Headers Grabber       │                              │
│ [18] > Domain to IP          │ [22] > Email Breach Check    │ [26] > Ping Tool             │                              │
│ [19] > DNS Resolver          │ [23] > MAC Address Lookup    │                              │                              │
│ [20] > GeoIP Tracker         │ [24] > Whois Lookup          │                              │                              │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
'''
    print(Colorate.Horizontal(Colors.cyan_to_blue, table))

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_banner()
    show_tool_table()

    try:
        choice = input(Fore.GREEN + "\nEntrez un numéro d'option (1 à 26) : ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= 26:
                send_to_webhook(f"L'utilisateur a exécuté l'option {num}")
                execute_script(num)
            else:
                print(Fore.RED + "[!] Numéro hors plage.")
                time.sleep(2)
                show_menu()
        else:
            print(Fore.RED + "[!] Veuillez entrer un chiffre.")
            time.sleep(2)
            show_menu()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Fermeture...")
        exit()

if __name__ == "__main__":
    while True:
        show_menu()
