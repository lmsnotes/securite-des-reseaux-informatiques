import os
import platform

class PingScanner:
    """Découverte d'hôtes via Ping Sweep """
    def scan(self, reseau_prefix):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        print(f"[*] Scan du réseau {reseau_prefix}.0/24...")
        for i in range(1, 255):
            ip = f"{reseau_prefix}.{i}"
            if os.system(f"ping {param} 1 -W 1 {ip} > /dev/null 2>&1") == 0:
                print(f"[+] Hôte trouvé : {ip}")

