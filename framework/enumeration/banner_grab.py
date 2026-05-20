import socket

class BannerGrabber:
    def grab(self, ip, port):
        port = int(port)
        print(f"[*] Tentative sur {ip}:{port}...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, port))

            # Si c'est du samba (139/445), on envoie une requête de négociation basique
            if port in [139, 445]:
                s.send(b'\x00\x00\x00\x2f\xff\x53\x4d\x42\x72\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x0c\x00\x02\x4e\x54\x20\x4c\x4d\x20\x30\x2e\x31\x32\x00')
            
            # Si c'est du HTTP (80)
            elif port == 80:
                s.send(b"HEAD / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")

            banner = s.recv(1024)
            s.close()

            if banner:
                readable_banner = banner.decode(errors='ignore').strip()
                print(f"[+] Données reçues : {readable_banner}")
                return readable_banner
            
        except Exception as e:
            print(f"[-] Impossible de récupérer la bannière : {e}")
            return None

