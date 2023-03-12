#Imports
import sys
import webbrowser
import subprocess
import os
import nmap
import requests
import tkinter as tk
import scapy.all as scapy
from tkinter import *
from tkinter import ttk
from prettytable import PrettyTable

# Fonction pour afficher le menu et demander à l'utilisateur de choisir une option
def menu_toolbox():
    print("")
    print("")
    print(" ################################################")
    print("  _______ ____   ____  _      ____   ______   __")
    print(" |__   __/ __ \ / __ \| |    |  _ \ / __ \ \ / /")
    print("    | | | |  | | |  | | |    | |_) | |  | \ V / ")
    print("    | | | |  | | |  | | |    |  _ <| |  | |> <| ")
    print("    | | | |__| | |__| | |____| |_) | |__| / . \ ")
    print("    |_|  \____/ \____/|______|____/ \____/_/ \_\ ")
    print("")
    print(" ################################################")
    print("")
    print("Menu:")
    print("1. Dorks")
    print("2. WebFinder")
    print("3. Scan NMAP")
    print("3. Scan NMAP CVE")
    print("4. Quitter")
    print("")

    choix = input("Entrez le numéro de l'option que vous souhaitez choisir: ")
    return choix

###################################### SCRIPT 1 - DORKS #########################

def executer_script1():

    def google_dork(query):
        # Ouvrir les résultats de recherche dans un navigateur
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new(url)

    # Boucle principale pour le menu
    while True:
        # Menu demandant à l'utilisateur de faire son choix sur 
        print("Choisissez une option:")
        print("1. Rechercher des documents PDF sur un site spécifique")
        print("2. Rechercher des pages contenant des mots de passe")
        print("3. Rechercher des pages vulnérables à l'injection SQL")
        print("4. Rechercher des pages contenant des adresses e-mail Gmail d'une personne")
        print("5. Rechercher les réseaux sociaux d'une personne")
        print("6. Rechercher des fichiers Excel contenant des mots de passe")
        print("7. Rechercher des pages contenant des vulnérabilités XSS")
        print("8. Rechercher des pages contenant des vulnérabilités LFI")
        print("9. Revenir au menu précédent")
        choice = input("Entrez votre choix (1-9): ")

        if choice == "1":
            keyword = input("Entrez le nom du site Web: ")
            query = f"site:{keyword} filetype:pdf"
            google_dork(query)
            
        elif choice == "2":
            keyword = input("Entrez un mot clé: ")
            query = f"intitle:\"Index of\" {keyword}"
            google_dork(query)
            
        elif choice == "3":
            keyword = input("Entrez un mot clé: ")
            query = f"inurl:\"id=\" AND \"SELECT\" {keyword}"
            google_dork(query)
            
        elif choice == "4":
            keyword = input("Entrez le nom de la personne : ")
            query = f"\"{keyword}\" intext:'gmail.com'"
            google_dork(query)
            
        elif choice == "5":
            keyword = input("Entrez le nom de la personne : ")
            query = f"\"{keyword}\" site:linkedin.com OR site:github.com OR site:facebook.com OR site:instagram.com OR site>"
            google_dork(query)
            
        elif choice == "6":
            keyword = input("Entrez un mot clé: ")
            query = f"intitle:\"Index of\" AND ext:xls {keyword}"
            google_dork(query)
            
        elif choice == "7":
            keyword = input("Entrez un mot clé: ")
            query = f"intitle:\"XSS\" OR intext:\"Cross Site Scripting\" {keyword}"
            google_dork(query)
            
        elif choice == "8":
            keyword = input("Entrez un mot clé: ")
            query = f"intitle:\"index of\" AND intext:\"../../\" {keyword}"
            google_dork(query)
            
        elif choice == "9":
            menu_toolbox()
            
        else:
            print("Choix invalide. Veuillez entrer un choix valide (1-9).")


###################################### SCRIPT 2 - WebFinder #########################

def executer_script2():
        # Boucle principale pour le menu

    def nikto():
        # Demander à l'utilisateur l'URL à scanner
        url = input("Entrez l'URL à scanner (ex : https://xxxxxxxx.fr) : ")

        # Commande pour exécuter Nikto
        nikto_command = "nikto -h " + url

        # Exécution de la commande Nikto avec subprocess
        nikto_result = subprocess.run(nikto_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Affichage du résultat de la commande Nikto
        print("Recherche en cours...")
        print("Cela peut prendre un certain temps ...")
        print(nikto_result.stdout.decode())

        # Demander à l'utilisateur s'il souhaite effectuer une recherche de répertoires avec Dirb
        response = input("Voulez-vous effectuer une recherche plus poussée de répertoires avec Dirb ? (O/N)")

        # Si l'utilisateur répond "Oui" ou "o", exécuter Dirb
        if response.lower() == "o":
            # Commande pour exécuter Dirb
            dirb_command = "dirb " + url + " /usr/share/wordlists/dirb/common.txt"

            # Exécution de la commande Dirb avec subprocess.Popen
            dirb_process = subprocess.Popen(dirb_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Affichage en temps réel de la sortie de Dirb
            while True:
                line = dirb_process.stdout.readline()
                if not line:
                    break
                print(line.decode().rstrip())

            # Fermeture du processus Dirb
            dirb_process.terminate()
            dirb_process.wait()

    while True:
        # Menu demandant à l'utilisateur de faire son choix sur 
        print("Choisissez une option:")
        print("1. Commencer la recherche")
        print("2. Revenir au menu précedent")
        choice = input("Entrez votre choix (1-2): ")

        if choice == "1":
            nikto()
            
        elif choice == "2":
            menu_toolbox()

###################################### SCRIPT 3 - NMAP #########################

def script_nmap():# Variable globale pour stocker l'empreinte du système d'exploitation
    
    def script_nmap_boucle():

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

    while True:
            # Menu demandant à l'utilisateur de faire son choix sur 
            print("Choisissez une option:")
            print("1. Commencer la recherche")
            print("2. Revenir au menu précedent")
            choice = input("Entrez votre choix (1-2): ")

            if choice == "1":
                script_nmap_boucle()
                
            elif choice == "2":
                menu_toolbox()

###################################### SCRIPT - NMAP CVE #########################

def nmapCVE():
    print("Exécution du script 4")
    # Ajoutez ici le code pour exécuter le script 3

# Boucle principale pour afficher le menu et exécuter les scripts
while True:
    choix = menu_toolbox()
    if choix == "1":
        executer_script1()
    elif choix == "2":
        executer_script2()
    elif choix == "3":
        executer_script3()
    elif choix == "4":
        sys.exit() # Quitter le programme
    else:
        print("Option invalide. Veuillez entrer un numéro entre 1 et 4.")