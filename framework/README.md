# Framework SRIE

**Auteurs :** Nina Perret & Lisa-Marie Durieux  
**Projet :** SRIE 
**Cible :** VISMIN (192.168.56.101)

---

## Description
Ce framework Python permet d'automatiser les 5 phases d'un Pentest. Il a été conçu pour automatiser le processus effectué manuellement dans le rapport.

### Fonctionnalités
Le framework est divisé en 5 phases via un menu interactif :

1.  **Reconnaissance**
    * **Whois Lookup** : Récupération des informations d'un domaine.
    * **Google Dorking** : Recherche avancée d'informations sensibles et de ressources exposées (OSINT).
    * **Shodan API** : attention nécessite une clé API shodan.
2.  **Scanning du réseau**
    * **Ping Sweep** : Identification des machines actives sur le réseau.
    * **Traceroute** : Analyse du chemin réseau.
    * **Nmap Scan** : Scan SYN rapide avec détection de versions (-sV).
3.  **Énumération**
    * **OS Detection** : Fingerprinting du système d'exploitation cible.
    * **Banner Grabbing** : Récupération des bannières de services (SSH, FTP, etc.).
4.  **Analyse de Vulnérabilités**
    * Vérification en local des versions de services (vsftpd, Apache, Samba) sur une base de CVE connues.
5.  **Exploitation**
    * **SSH Brute Force** : Avec 'paramiko'
    * **FTP Brute Force** : Avec 'hydra'
    * **Tomcat Brute Force** : Avec 'hydra'

---

## Installation

### 1. Pré-requis Système (Kali / Linux)
Ce projet utilise des outils externes. Ils doivent être installés sur la machine.
sudo apt update
sudo apt install nmap hydra traceroute whois -y

### 2. Installation de l'environnement Python
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

---

## Lancement

sudo python3 main.py
Suivre les instructions du menu

