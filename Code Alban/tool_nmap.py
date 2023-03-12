import nmap
import requests
import tkinter as tk
import scapy.all as scapy
from tkinter import *
from tkinter import ttk
from prettytable import PrettyTable

# Variable globale pour stocker l'empreinte du système d'exploitation
os_fingerprint = ''

# Créer la fenêtre principale
root = Tk()

# Changer le titre de la fenêtre
root.wm_title("Script de Alban et Erwan")

# Créer un widget `ttk.Notebook` pour contenir les onglets.
notebook = ttk.Notebook(root)

# Créer un onglet pour le scan nmap
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Scan NMAP")

tab2= ttk.Frame(notebook)
notebook.add(tab2, text="Scan Réseau")

# Afficher la barre de progression lorsque le scan commence
def start_scan():
  progress_bar.start()

# Arrêtez la barre de progression lorsque le balayage est terminé.
def stop_scan():
  progress_bar.stop()

# ------------------- Onglet 1 : Scan NMAP -------------------
# Créer une étiquette et un champ de saisie pour l'adresse IP
ip_label = tk.Label(tab1, text="Adresse IP:")
ip_label.pack()
ip_entry = Entry(tab1)
ip_entry.pack()

#Variable permettant de stocker l'état du mode de balayage sélectionné (Vrai pour le mode rapide, Faux pour le mode complet).
fast_scan_var = tk.BooleanVar()
fast_scan_checkbox = tk.Checkbutton(tab1, text="Mode rapide", variable=fast_scan_var)
fast_scan_checkbox.pack()

#Créer une barre de progression pour montrer la progression du scan
progress_bar = tk.ttk.Progressbar(tab1, mode='determinate')

#Initialiser un scanner de port nmap
scanner = nmap.PortScanner()

#Fonction permettant de lancer l'analyse NMAP
#Effectuer un balayage NMAP lorsque le bouton est cliqué.
def scan_nmap():
  start_scan()

  # Obtenir l'adresse IP entrée par l'utilisateur
  ip_address = ip_entry.get()

  # Initialiser un scanner de port nmap
  scanner = nmap.PortScanner()
  # Définir les options de numérisation en fonction du mode de numérisation sélectionné.
  if fast_scan_var.get():
    # Effectuer un scan rapide avec l'option -T4
    scan_options = '-T5 -F'
  else:
        # Effectuer un scan complet avec l'option -sV
    scan_options = '-T5 -sV'

  # Effectuer le scan nmap avec les options choisies
  scanner.scan(ip_address, arguments=scan_options)

  # Effacer les données des tables
  scan_table.delete(*scan_table.get_children())

  # Afficher uniquement les ports ouverts avec leur nom et leur version dans la table NMAP Scan.
  for port in scanner[ip_address].all_tcp():
    scan_table.insert('', 'end', values=(port, scanner[ip_address].tcp(port)['name'], scanner[ip_address].tcp(port)['version'], 'TCP'))
  for port in scanner[ip_address].all_udp():
    scan_table.insert('', 'end', values=(port, scanner[ip_address].udp(port)['name'], scanner[ip_address].udp(port)['version'], 'UDP'))

  stop_scan()

#Créer un bouton pour démarrer le scan NMAP
nmap_button = ttk.Button(tab1, text="Lancer le scan", command=scan_nmap)
nmap_button.pack()

#Créer une table pour afficher les résultats du scan NMAP
scan_table = ttk.Treeview(tab1, columns=("Ports", "Services", "Versions"))
scan_table.heading("#0", text="")
scan_table.heading("#1", text="Ports")
scan_table.heading("#2", text="Services")
scan_table.heading("#3", text="Versions")
scan_table.column("#0", width=10, anchor="center", stretch=True)
scan_table.column("#1", width=50, anchor="center", stretch=True)
scan_table.column("#2", width=150, anchor="center", stretch=True)
scan_table.column("#3", width=100, anchor="center", stretch=True)
scan_table.pack()

# ------------------- Onglet 2 : Scan Réseau -------------------

# Fonction pour récupérer les informations sur l'OS d'une adresse IP
def get_os_info(ip, use_nmap=False):
    if not use_nmap:
        try:
            ans, unans = scapy.sr(IP(dst=ip)/TCP(dport=80,flags="S"),timeout=2,verbose=0)
            os = ans[0][1][1].fields['osmatch'][0].name
        except:
            os = "Unknown"
    else:
        nm = nmap.PortScanner()
        nm.scan(ip, arguments='-O')
        os = 'Unknown'
        if 'osclass' in nm[ip]:
            os = nm[ip]['osclass'][0]['osfamily']
    return os

# Fonction pour scanner le réseau
def scan_network():
    ip = ip_entry_2.get()
    scan_result = []
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    for element in answered_list:
        ip = element[1].psrc
        mac = element[1].hwsrc
        os = get_os_info(ip)
        scan_result.append((ip, mac, os))
    show_results(scan_result)

# Fonction pour filtrer les résultats en fonction de l'état de la connexion
def filter_results():
    filtered_results = []
    for result in scan_result:
        if result[2] == state_filter.get():
            filtered_results.append(result)
    show_results(filtered_results)

# Fonction pour afficher les résultats
def show_results(results):
    table.delete(*table.get_children())
    for result in results:
        table.insert("", "end", values=result)

# Création du champ de saisie pour l'adresse IP
ip_frame = Frame(tab2)
ip_label_2 = Label(ip_frame, text="IP_ADDRESS/MASK:")
ip_label_2.pack(side=LEFT)
ip_entry_2 = Entry(ip_frame)
ip_entry_2.pack(side=LEFT)
ip_frame.pack()

# Création du bouton de scan
scan_button = Button(tab2, text="Scan", command=scan_network)
scan_button.pack()

# Création du menu déroulant pour l'état de la connexion
state_frame = Frame(tab2)
state_label = Label(state_frame, text="Connection State:")
state_label.pack(side=LEFT)
state_filter = ttk.Combobox(state_frame, values=["Open", "Closed"])
state_filter.pack(side=LEFT)
state_button = Button(state_frame, text="Filter", command=filter_results)
state_button.pack(side=LEFT)
state_frame.pack()

# Création du tableau pour afficher les résultats
table_frame = Frame(tab2)
table = ttk.Treeview(table_frame, columns=("IP Address", "MAC Address", "OS"))
table.heading("IP Address", text="IP Address")
table.heading("MAC Address", text="MAC Address")
table.heading("OS", text="OS")
table.pack(fill=BOTH, expand=YES, side=RIGHT)
table_frame.pack(fill=BOTH, expand=YES, side=RIGHT)

# ------------------- Mise en page -------------------

# Créez un contrôle d'onglet pour contenir les trois onglets.
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill='both')

# Ajouter les onglets à la fenêtre
notebook.pack()

# Exécuter la boucle principale
root.mainloop()

