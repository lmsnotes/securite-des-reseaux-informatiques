import shodan

class ShodanTool:
    """Interroge Shodan pour l'infrastructure """
    def __init__(self, api_key):
        self.api = shodan.Shodan(api_key)

    def search_host(self, ip):
        try:
            host = self.api.host(ip)
            print(f"IP: {ip}\nPorts: {host['ports']}")
        except Exception as e:
            print(f"Erreur Shodan: {e}")

