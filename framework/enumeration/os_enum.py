import nmap

class OSError:
    pass

class OSEnumerator:
    """Outil de détection du système d'exploitation (Session 05 - Task #7)"""

    def __init__(self):
        self.nm = nmap.PortScanner()

    def detect_os(self, ip):
        """Tente d'identifier l'OS de la cible via fingerprinting"""
        print(f"[*] Analyse du système d'exploitation pour {ip}...")
        try:
            scan_results = self.nm.scan(ip, arguments="-O")
            
            if 'osmatch' in scan_results['scan'][ip]:
                for match in scan_results['scan'][ip]['osmatch']:
                    os_name = match['name']
                    accuracy = match['accuracy']
                    
                    print(f"[+] OS détecté : {os_name} (Précision : {accuracy}%)")
                    
                    if 'osclass' in match:
                        device_type = match['osclass'][0]['type']
                        print(f"    Type de matériel : {device_type}")
                    
                    return os_name
            else:
                print("[-] Impossible de déterminer l'OS avec certitude.")
                return "Inconnu"
                
        except Exception as e:
            print(f"[-] Erreur lors de la détection d'OS : {e}")
            print("    Note : La détection d'OS nécessite souvent des privilèges root (sudo).")
            return None

