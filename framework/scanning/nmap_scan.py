import nmap

class NmapScanner:
    """Scan de ports avec détection de services (Session 04 - Task #3) [cite: 1232]"""
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan_ports(self, ip):
        # Scan SYN (-sS) avec détection de version (-sV) 
        print(f"[*] Scan Nmap sur {ip}...")
        self.nm.scan(ip, arguments='-sS -sV')
        for proto in self.nm[ip].all_protocols():
            for port in self.nm[ip][proto].keys():
                state = self.nm[ip][proto][port]['state']
                print(f"Port {port}: {state}")

