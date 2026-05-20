import webbrowser
import os

class GoogleDorker:
    def search_admin(self, cible):
        query = f"site:{cible} intitle:admin | inurl:login"
        url = f"https://www.google.com/search?q={query}"
        
        print(f"\n[!] Requête générée : {url}")
        
        # On tente d'ouvrir, si ça échoue (erreur sudo), l'utilisateur a le lien
        try:
            # On vérifie si on est en root, si oui on prévient
            if os.geteuid() == 0:
                print("[i] Note : Copiez-collez le lien ci-dessus dans votre navigateur (Sudo bloque l'ouverture automatique).")
            webbrowser.open(url)
        except:
            pass

