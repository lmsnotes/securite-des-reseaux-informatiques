class VulnerabilityScanner:
    """Outil d'analyse de vulnérabilités """

    def __init__(self):
    #d'après CVE
        self.vulnerability_db = {
            "vsftpd 2.3.4": "CVE-2011-2523 - Backdoor détecté (Exécution de code à distance)",
            "Apache httpd 2.2.8": "Plusieurs vulnérabilités de déni de service (DoS)",
            "Samba 3.0.20": "CVE-2007-2447 - MS-RPC Remote Command Injection",
            "OpenSSH 4.7p1": "Vulnérabilité potentielle liée aux anciennes méthodes d'authentification"
        }

    def analyze_service(self, service_name, version):
        """Compare un service et sa version avec la base de vulnérabilités"""
        print(f"[*] Analyse de vulnérabilité pour : {service_name} {version}...")
        
        match_key = f"{service_name} {version}"
        
        # Recherche d'une correspondance exacte ou partielle
        found_vuln = None
        for key in self.vulnerability_db:
            if key.lower() in match_key.lower():
                found_vuln = self.vulnerability_db[key]
                break
        
        if found_vuln:
            print(f"[!] DANGER : {found_vuln}")
            return found_vuln
        else:
            print("[+] Aucune vulnérabilité critique connue trouvée dans la base locale.")
            return None

    def check_weak_credentials(self, service):
        """Suggère des tests de mots de passe par défaut"""

        defaults = {
            "ftp": "admin/admin, anonymous/anonymous",
            "ssh": "root/toor, user/user",
            "postgresql": "postgres/postgres"
        }
        if service.lower() in defaults:
            print(f"[i] Suggestion : Testez les identifiants par défaut : {defaults[service.lower()]}")

