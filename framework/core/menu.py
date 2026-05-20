class Menu:
    def __init__(self):
        self.options = {
            "1": "Reconnaissance / Footprinting",
            "2": "Scanning Networks",
            "3": "Enumeration",
            "4": "Vulnerability Analysis",
            "5": "Gaining Access",
            "q": "Quitter"
        }

    def afficher_banner(self):
        print("-" * 40)
        print("   FRAMEWORK NINA PERRET & LISA-MARIE DURIEUX   ")
        print("-" * 40)

    def afficher_principal(self):
        self.afficher_banner()
        for key, value in self.options.items():
            print(f"[{key}] {value}")
        print("-" * 40)

    def recuperer_choix(self):
        return input("Choisissez une option : ")
