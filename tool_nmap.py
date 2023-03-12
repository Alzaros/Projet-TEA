#Modules nécessaires
import nmap  # Importation du module nmap pour effectuer des scans de ports
import requests  # Importation du module requests pour envoyer des requêtes HTTP
import tkinter as tk  # Importation du module tkinter pour créer une interface graphique
import scapy.all as scapy  # Importation du module scapy pour effectuer des opérations de réseau
from tkinter import *  # Importation des classes et fonctions de base de tkinter
from tkinter import ttk  # Importation des widgets supplémentaires de tkinter
from prettytable import PrettyTable  # Importation du module prettytable pour afficher des tableaux de données
from scapy.layers.l2 import ARP  # Importation de la classe ARP de la couche 2 de scapy pour effectuer des opérations de résolution d'adresse MAC


# Variable globale pour stocker l'empreinte du système d'exploitation
os_fingerprint = ''

# Créer la fenêtre principale
root = Tk()

# Changer le titre de la fenêtre
root.wm_title("Script de Alban et Erwan")

# Créer un widget `ttk.Notebook` pour contenir les onglets.
notebook = ttk.Notebook(root)

# Créer un onglet pour le scan nmap
page1 = ttk.Frame(notebook)
notebook.add(page1, text="Scan NMAP")

# Créer un onglet pour le scan réseau
page2 = ttk.Frame(notebook)
notebook.add(page2, text="Scan Réseau")

# Afficher la barre de progression lorsque le scan commence
def debut_scan():
    progress_bar.start()

# Arrêtez la barre de progression lorsque le balayage est terminé.
def fin_scan():
    progress_bar.stop()

# ------------------- Onglet 1 : Scan NMAP -------------------

# Créer une étiquette et un champ de saisie pour l'adresse IP
texte_ip1 = tk.Label(page1, text="Adresse IP:")
texte_ip1.pack()
zone_ip1 = Entry(page1)
zone_ip1.pack()

# Variable permettant de stocker l'état du mode de balayage sélectionné (Vrai pour le mode rapide, Faux pour le mode complet).
scan_rapide_var = tk.BooleanVar()
scan_rapide_checkbox = tk.Checkbutton(page1, text="Mode rapide", variable=scan_rapide_var)
scan_rapide_checkbox.pack()

# Créer une barre de progression pour montrer la progression du scan
progress_bar = tk.ttk.Progressbar(page1, mode='determinate')

# Initialiser un scanner de port nmap
scanner = nmap.PortScanner()

# Fonction permettant de lancer l'analyse NMAP
# Effectuer un balayage NMAP lorsque le bouton est cliqué.
def scan_nmap():
    debut_scan()

    # Obtenir l'adresse IP entrée par l'utilisateur
    adresse_ip = zone_ip1.get()

    # Initialiser un scanner de port nmap
    scanner = nmap.PortScanner()

    # Définir les options de numérisation en fonction du mode de numérisation sélectionné.
    if scan_rapide_var.get():
        # Effectuer un scan rapide avec l'option -T4
        scan_options = '-T5 -F'
    else:
        # Effectuer un scan complet avec l'option -sV
        scan_options = '-T5 -sV'

    # Effectuer le scan nmap avec les options choisies
    scanner.scan(adresse_ip, arguments=scan_options)

    # Effacer les données des tables
    scan_table.delete(*scan_table.get_children())

    # Afficher uniquement les ports ouverts avec leur name et leur version dans la table NMAP Scan.
    for port in scanner[adresse_ip].all_tcp():
        scan_table.insert('', 'end', values=(port, scanner[adresse_ip].tcp(port)['name'], scanner[adresse_ip].tcp(port)['version'], 'TCP'))
    for port in scanner[adresse_ip].all_udp():
        scan_table.insert('', 'end', values=(port, scanner[adresse_ip].udp(port)['name'], scanner[adresse_ip].udp(port)['version'], 'UDP'))

    fin_scan()

#Créer un bouton pour démarrer le scan NMAP
bouton_nmap = ttk.Button(page1, text="Lancer le scan", command=scan_nmap)
bouton_nmap.pack()

#Créer une table pour afficher les résultats du scan NMAP
scan_table = ttk.Treeview(page1, columns=("Ports", "Services", "Versions"))
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

# Créer une étiquette et un champ de saisie pour l'adresse IP et le masque
texte_ip2 = tk.Label(page2, text="AdresseIP/Masque:")
texte_ip2.pack()
zone_ip2 = Entry(page2)
zone_ip2.pack()

#Fonction pour scanner le réseau
def scan_reseau():
  # Récupérer l'adresse IP et le masque entrés par l'utilisateur
  ip = zone_ip2.get()
  resultat_scan = []
  # Effectuer une requête ARP pour obtenir les adresses IP et MAC des hôtes connectés au réseau
  requete_arp = scapy.ARP(pdst=ip)
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  requete_arp_broadcast = broadcast/requete_arp
  liste_reponse = scapy.srp(requete_arp_broadcast, timeout=1, verbose=False)[0]
  # Ajouter chaque adresse IP et MAC à la liste des résultats
  for element in liste_reponse:
    ip = element[1].psrc
    mac = element[1].hwsrc
    resultat_scan.append((ip, mac))
  # Afficher les résultats dans la table
  show_results(resultat_scan)

#Fonction pour afficher les résultats dans la table
def show_results(resultats):
  # Effacer les résultats précédents de la table
  scanreseau_table.delete(*scanreseau_table.get_children())
  # Ajouter chaque adresse IP et MAC à la table
  for resultat in resultats:
    scanreseau_table.insert('', 'end', values=resultat)

#Créer un bouton pour lancer le scan du réseau
bouton_reseau = ttk.Button(page2, text="Lancer le scan", command=scan_reseau)
bouton_reseau.pack()

#Créer une table pour afficher les résultats du scan réseau
scanreseau_table = ttk.Treeview(page2, columns=('Adresse IP', 'Adresse MAC'))
scanreseau_table.heading('#0', text='')
scanreseau_table.heading('#1', text='Adresse IP')
scanreseau_table.heading('#2', text='Adresse MAC')
scanreseau_table.column('#0', width=1, anchor='center', stretch=True)
scanreseau_table.column('#1', width=150, anchor='center', stretch=True)
scanreseau_table.column('#2', width=150, anchor='center', stretch=True)
scanreseau_table.pack()

# ------------------- Mise en page -------------------

# Ajouter les onglets à la fenêtre
notebook.pack()

# Exécuter la boucle principale
root.mainloop()
