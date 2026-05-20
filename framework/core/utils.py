import os

def clear_screen():
    """Nettoie le terminal selon l'OS"""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_ip(ip):
    """Vérification sommaire du format de l'IP"""
    parts = ip.split('.')
    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)
