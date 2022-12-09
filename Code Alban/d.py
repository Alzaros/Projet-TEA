# Importer nmap et Tkinter
import nmap
from tkinter import *
from tkinter import ttk


# Créer la fenêtre principale
root = Tk()

# Fonction pour effectuer un scan nmap lorsque le bouton est cliqué
def scan_nmap():
  # Récupérer l'adresse IP entrée par l'utilisateur
  ip_address = ip_entry.get()

  # Initialiser un scanneur de ports nmap
  scanner = nmap.PortScanner()

  # Effectuer un scan nmap avec l'option -sV pour obtenir des informations sur les ports ouverts et les services en cours d'exécution sur l'hôte cible
  scanner.scan(ip_address, arguments='-sV')

  # Effacer les données des tableaux
  scan_table.delete(*scan_table.get_children())
  cve_table.delete(*cve_table.get_children())

  # Afficher uniquement les ports ouverts avec leur nom et leur version dans le tableau Scan NMAP
  for port in scanner[ip_address].all_tcp():
    scan_table.insert('', 'end', values=(port, scanner[ip_address].tcp(port)['name'], scanner[ip_address].tcp(port)['version']))
  for port in scanner[ip_address].all_udp():
    scan_table.insert('', 'end', values=(port, scanner[ip_address].udp(port)['name'], scanner[ip_address].udp(port)['version']))

  # TODO: Récupérer les informations CVE pour chaque service en cours d'exécution sur l'hôte cible et les afficher dans le tableau CVE

# Créer un label pour demander à l'utilisateur d'entrer l'adresse IP à scanner
ip_label = Label(root, text="Entrez l'adresse IP à scanner :")
ip_label.pack()

# Créer un champ de texte pour que l'utilisateur entre l'adresse IP
ip_entry = Entry(root)
ip_entry.pack()

# Créer un bouton pour démarrer le scan nmap lorsqu'il est cliqué
scan_button = Button(root, text="Scanner avec nmap", command=scan_nmap)
scan_button.pack()

# Créer un tableau pour afficher les résultats du scan nmap
scan_table = ttk.Treeview(root, columns=('Port', 'Service', 'Version'), show='headings')
scan_table.pack()
scan_table.heading('Port', text="Port")
scan_table.heading('Service', text="Service")
scan_table.heading('Version', text="Version")

# Créer un tableau pour afficher les informations CVE
cve_table = ttk.Treeview(root, columns=('CVE ID','Description'), show='headings')
cve_table.pack()
cve_table.heading('CVE ID', text="CVE ID")
cve_table.heading('Description', text="Description")

# Afficher la fenêtre principale
root.mainloop()
