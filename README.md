# securite-des-reseaux-informatiques
Python-based penetration testing framework developed for ethical hacking and network security labs, featuring reconnaissance, scanning, enumeration, vulnerability analysis, and exploitation modules.

## Overview

This project was developed as part of the *Sécurité des Réseaux Informatiques d’Entreprise* course. 

The goal of this project is to design and implement a modular penetration testing framework in Python while applying the concepts studied during ethical hacking labs.

The framework reproduces the main phases of a professional penetration test:

1. Reconnaissance / Footprinting  
2. Network Scanning  
3. Enumeration  
4. Vulnerability Analysis  
5. Gaining Access  

The project also includes reporting and practical experimentation performed in a controlled lab environment using the VISMIN vulnerable virtual machine.

---

# Objectives

The main objectives of this project are:

- Understand penetration testing methodologies
- Learn how ethical hacking tools operate
- Automate common security testing tasks
- Practice network security analysis safely
- Develop maintainable and modular Python code
- Build a reusable cybersecurity framework

---

# Technologies Used

## Programming Language
- Python 3.x

## Main Tools
- Wireshark
- Nmap
- Nessus
- Ghidra
- Metasploit
- Social Engineering Toolkit (SET)
- DNSRecon
- DNSEnum

---

# Project Structure

```bash
pen_test_framework/
│
├── main.py
│
├── core/
│   ├── menu.py
│   ├── utils.py
│   └── config.py
│
├── reconnaissance/
│   ├── whois_lookup.py
│   ├── shodan_search.py
│   ├── osint_ghdb.py
│   └── phishing_simulation.py
│
├── scanning/
│   ├── ping_scan.py
│   ├── nmap_scan.py
│   ├── traceroute.py
│   └── port_scan.py
│
├── enumeration/
│   ├── banner_grab.py
│   ├── os_enum.py
│   └── user_enum.py
│
├── vulnerabilities/
│   ├── vuln_scanner.py
│   └── nessus_parser.py
│
├── exploitation/
│   ├── ftp_exploit.py
│   ├── ssh_bruteforce.py
│   └── metasploit_launcher.py
│
├── reports/
│   └── report_generator.py
│
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone <repository_url>
cd pen_test_framework
```

## Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run the framework using:

```bash
python3 main.py
```

The framework provides a command-line interface allowing navigation through the different penetration testing modules.

---

# Features

## 1. Reconnaissance / Footprinting

- WHOIS lookup
- DNS reconnaissance
- Shodan search
- Google Hacking Database queries
- Social engineering simulations

Example:

```bash
python3 reconnaissance/whois_lookup.py example.com
```

---

## 2. Network Scanning

- Ping sweep
- Port scanning
- Traceroute
- Nmap automation

Example:

```bash
python3 scanning/nmap_scan.py 192.168.1.10
```

---

## 3. Enumeration

- Banner grabbing
- OS detection
- User enumeration
- Service fingerprinting

Example:

```bash
python3 enumeration/banner_grab.py 192.168.1.10 80
```

---

## 4. Vulnerability Analysis

- Nessus integration
- Vulnerability scanning
- CVE correlation
- Searchsploit integration

Example:

```bash
python3 vulnerabilities/vuln_scanner.py 192.168.1.10
```

---

## 5. Gaining Access

- FTP exploitation
- SSH brute force simulation
- Metasploit automation
- Exploit testing against VISMIN

Example:

```bash
python3 exploitation/ftp_exploit.py 192.168.1.10
```

---

# Reverse Engineering Challenge

This project also includes reverse engineering exercises using Ghidra.

Objectives include:

- Binary analysis
- Program behavior analysis
- Validation logic reconstruction
- Flag recovery
- Binary patching

---

# Virtual Lab Environment

The framework was tested in a controlled virtual environment composed of:

- A Linux attacker machine (Kali Linux or Ubuntu)
- The VISMIN vulnerable VM

## Recommended Configuration

- Host-Only network mode for isolated testing
- Bridged mode only in private networks
- Never expose VISMIN to the public Internet

---

# Ethical and Legal Notice

This framework was developed exclusively for educational purposes in a controlled laboratory environment.

Unauthorized scanning, exploitation, or access to systems without permission is illegal and unethical.

The authors assume no responsibility for misuse of this project.

---

# Software Engineering Practices

The project follows good development practices:

- Modular architecture
- Object-Oriented Programming (OOP)
- PEP 8 coding style
- Reusable components
- Structured CLI output
- Dependency management with `requirements.txt`

---

# Future Improvements

Possible future improvements include:

- Web interface
- Database integration
- PDF report generation
- Additional exploitation modules
- Real-time monitoring dashboards

---

# Authors

Developed as part of the *Sécurité des Réseaux Informatiques d’Entreprise* course.

---

# References

- https://www.python.org/doc/
- https://nmap.org/docs.html
- https://www.wireshark.org/docs/
- https://owasp.org/
- https://docs.metasploit.com/
