import socket
import termcolor
import threading
import sys
from pyfiglet import figlet_format

def print_banner():
    banner = figlet_format("DEFINITLY")
    print(termcolor.colored(banner, 'blue'))
    banner = figlet_format("Port-Scanner")
    print(termcolor.colored(banner, 'blue'))
    print(termcolor.colored("DEFINITLY - Scanner de ports en Python", 'yellow'))
    print(termcolor.colored("Auteur: @HoussamElBouamraoui", 'yellow'))
    print(termcolor.colored("GitHub: https://github.com/Houssam-01", 'yellow'))

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(termcolor.colored(f"[+] Port {port} ouvert sur {ip}", 'green'))
        sock.close()
    except Exception:
        pass

def scan(ip, ports):
    print(termcolor.colored(f"\n[+] Démarrage du scan pour {ip}", 'blue'))
    threads = []
    
    for port in range(1, ports + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    print_banner()
    while True:
        print("\n---Menu---")
        print("| 1 - Lancer un scan")
        print("| 0 - Quitter")
        choix = input("\n[*] Entrez votre choix : ")
        
        if choix == '1':
            targets = input("[*] Entrez les cibles à scanner (séparées par des virgules) : ")
            ports = int(input("[*] Nombre de ports à scanner (ex: 100) : "))
            
            if ',' in targets:
                print(termcolor.colored("[*] Scan de plusieurs cibles...", 'yellow'))
                for ip in targets.split(','):
                    scan(ip.strip(), ports)
            else:
                scan(targets.strip(), ports)
        
        elif choix == '0':
            print(termcolor.colored("Merci d'avoir utilisé Port-scanner . À bientôt !", 'red'))
            sys.exit()
        
        else:
            print(termcolor.colored("[!] Choix invalide, veuillez réessayer.", 'red'))

if __name__ == "__main__":
    main()
