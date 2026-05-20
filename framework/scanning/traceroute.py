import os
import platform

class TracerouteTool:
    """Outil de diagnostic réseau pour cartographier le chemin vers la cible"""
    
    def run(self, cible):
        """Exécute un traceroute vers une IP ou un nom de domaine"""
        print(f"[*] Analyse du chemin réseau vers {cible}...")
        
        # Sur Linux, on utilise la commande 'traceroute'
        # Sur Windows, la commande est 'tracert'
        cmd = "tracert" if platform.system().lower() == "windows" else "traceroute"
        
        try:
            resultat = os.popen(f"{cmd} {cible}").read()
            print(resultat)
            
            return resultat
        except Exception as e:
            print(f"Erreur lors du traceroute : {e}")
            return None

