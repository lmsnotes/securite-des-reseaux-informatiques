import sys
import os
from core import Menu, clear_screen, validate_ip
from reconnaissance.whois_lookup import WhoisTool
from reconnaissance.osint_ghdb import GoogleDorker
from reconnaissance.shodan_search import ShodanTool
from scanning.ping_scan import PingScanner
from scanning.nmap_scan import NmapScanner
from scanning.traceroute import TracerouteTool
from enumeration.banner_grab import BannerGrabber
from enumeration.os_enum import OSEnumerator
from vulnerabilities.vuln_scanner import VulnerabilityScanner
from exploitation.ftp_bruteforce import FTPBruteForce
from exploitation.ssh_bruteforce import SSHBruteForce
from exploitation.tomcat_bruteforce import TomcatBruteForce

def main():
    menu = Menu()
    clear_screen()
    
    while True:
        menu.afficher_principal()
        choix = menu.recuperer_choix()

        # 1. RECONNAISSANCE
        if choix == "1":
            print("\n--- Phase 1 : Reconnaissance ---")
            print("\nChoix de la méthode :")
            print("1. whois")
            print("2. google dorking")
            print("3. shodan")
            methode = input("\nOption choisie : ")
            
            if methode == "1":
                cible = input("Entrez le nom du domaine (ex: emse.fr) pour whois : ")
                WhoisTool().lookup(cible)
            elif methode == "2":
                cible = input("Entrez la cible pour Google Dorking : ")
                GoogleDorker().search_admin(cible)
            elif methode == "3":
                cible = input("Entrez l'IP pour Shodan : ")
                cle_api = input("Entrez votre clé API Shodan : ") 
                if cle_api.strip():
                    shodan_tool = ShodanTool(cle_api) 
                    shodan_tool.search_host(cible)
                else:
                    print("[-] Clé API vide, abandon de la recherche Shodan.")

        # 2. SCANNING 
        elif choix == "2":
            print("\n--- Phase 2 : Scanning Networks ---")
            print("\nChoix de la méthode :")
            print("1. Ping Sweep (Réseau)")
            print("2. Traceroute")
            print("3. Nmap Scan (Ports)")
            methode_scan = input("\nOption choisie : ")

            if methode_scan == "1":
                prefix = input("Entrez le préfixe réseau (ex: 192.168.56) : ")
                PingScanner().scan(prefix)

            elif methode_scan == "2":
                target = input("\nEntrez l'IP de VISMIN pour Traceroute (ex: 192.168.56.101): ")
                TracerouteTool().run(target)

            elif methode_scan == "3":
                target = input("\nEntrez l'IP cible pour le scan Nmap : ")
                if validate_ip(target):
                    NmapScanner().scan_ports(target)
                else:
                    print("[-] Adresse IP invalide.")

        # 3. ENUMERATION 
        elif choix == "3":
            print("\n--- Phase 3 : Enumeration ---")
            print("\nChoix de la méthode :")
            print("1. OS Detection")
            print("2. Banner Grabbing")
            methode_enum = input("\nOption choisie : ")

            if methode_enum == "1":
                ip = input("Entrez l'IP de VISMIN pour la détection d'OS (ex: 192.168.56.101): ")
                OSEnumerator().detect_os(ip)

            elif methode_enum == "2":
                ip = input("Entrez l'IP de la cible : ")
                port = input("Port à énumérer (ex: 21, 22) pour le banner grabbing : ")
                BannerGrabber().grab(ip, port)

        # 4. VULNERABILITY ANALYSIS 
        elif choix == "4":
            print("\n--- Phase 4 : Vulnerability Analysis ---")
            service = input("Nom du service (ex: vsftpd) : ")
            version = input("Version du service (ex: 2.3.4) : ")
            VulnerabilityScanner().analyze_service(service, version)
            
        # 5. GAINING ACCESS
        elif choix == "5":
            print("\n--- Phase 5 : Gaining Access ---")
            ip = input("Entrez l'IP de VISMIN (ex: 192.168.56.101): ")
            print("\nChoix de l'attaque :")
            print("1. Brute Force SSH ")
            print("2. Brute Force FTP")
            print("3. Brute Force Tomcat")
            methode = input("\nOption choisie : ")

            if methode == "1":
                if os.path.exists("exploitation/usernames.txt") and os.path.exists("exploitation/passwords.txt"):
                    ssh_tool = SSHBruteForce()
                    print(f"[*] Début du Brute Force SSH sur {ip}...")
                    found = False
                    with open("exploitation/usernames.txt", "r") as u_file:
                        for user in u_file:
                            if found: break
                            user = user.strip()
                            with open("exploitation/passwords.txt", "r") as p_file:
                                for pwd in p_file:
                                    pwd = pwd.strip()
                                    if ssh_tool.test_credentials(ip, user, pwd):
                                        found = True
                                        break
                    if not found: print("[-] Aucun accès trouvé.")
                else:
                    print("[-] Erreur : Les fichiers .txt (usernames/passwords) manquent.")

            elif methode == "2":
                ftp_tool = FTPBruteForce(ip)
                ftp_tool.run_hydra()
                
            elif methode == "3":
                    tomcat_tool = TomcatBruteForce(ip)
                    tomcat_tool.run_hydra() 
                    
	# OPTION QUITTER 
        elif choix.lower() == "q":
            print("\n[!] Arrêt du Framework  ")
            sys.exit()       

if __name__ == "__main__":
    main()

