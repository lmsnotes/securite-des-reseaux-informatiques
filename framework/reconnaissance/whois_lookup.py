import whois

class WhoisTool:
    """Récupère les données d'enregistrement de domaine (Session 03 - Task #3) [cite: 829]"""
    def lookup(self, domaine):
        try:
            print(f"[*] Recherche WHOIS pour : {domaine}...")
            info = whois.whois(domaine)
            resultat = f"Registrar: {info.registrar}\nServeurs: {info.name_servers}"
            print(resultat)
            return resultat
        except Exception as e:
            return f"Erreur : {e}"

