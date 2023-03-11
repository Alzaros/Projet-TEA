import nmap
import tkinter as tk
from tkinter import ttk

# Créer une instance de l'objet nmap.PortScanner()
nm = nmap.PortScanner()

# Définir les colonnes pour le tableau
columns = ("Port", "Protocol", "CVE")

def scan_ports(ip_address):
    # Scanner les ports ouverts sur l'adresse IP donnée en utilisant le script vulners de Nmap
    nm.scan(hosts=ip_address, arguments='-sV --script vulners')

    port_cve_list = []
    # Itérer sur les ports ouverts pour récupérer les CVE
    for port in nm[ip_address]['tcp'].keys():
        port_info = nm[ip_address]['tcp'][port]
        protocol = port_info['name']
        product = port_info['product']
        version = port_info['version']
        cve_list = port_info.get('script', {}).get('vulners', {}).get('CVE', [])
        cve_list = ', '.join(cve_list) if cve_list else '-'
        port_cve_list.append((port, protocol, cve_list))

    return port_cve_list

def display_results():
    # Obtenir l'adresse IP à partir de l'entrée utilisateur
    ip_address = ip_entry.get()

    # Scanner les ports et récupérer les CVE
    port_cve_list = scan_ports(ip_address)

    # Vider le tableau s'il contient déjà des résultats
    for row in table.get_children():
        table.delete(row)

    # Ajouter les résultats au tableau
    for port_cve in port_cve_list:
        table.insert("", tk.END, values=port_cve)

    # Si aucun CVE n'a été trouvé, afficher un message d'information
    if not any(cve != '-' for _, _, cve in port_cve_list):
        table.insert("", tk.END, values=("Aucun CVE trouvé", "", ""))

def quit_program():
    root.destroy()

def restart_program():
    root.destroy()
    execv(sys.executable, ['python'] + sys.argv)

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Nmap CVE Scanner")

# Ajouter une étiquette pour saisir l'adresse IP
ip_label = tk.Label(root, text="Adresse IP:")
ip_label.grid(row=0, column=0)

# Ajouter une entrée pour l'adresse IP
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1)

# Ajouter un bouton pour lancer le scan
scan_button = tk.Button(root, text="Scan", command=display_results)
scan_button.grid(row=1, column=0)

# Créer un tableau pour afficher les résultats
table = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    table.heading(col, text=col)
table.grid(row=3, columnspan=2)

# Ajouter un bouton Quitter
quit_button = tk.Button(root, text="Quitter", command=quit_program)
quit_button.grid(row=2, column=0)

# Ajouter un bouton pour relancer le programme
restart_button = tk.Button(root, text="Relancer", command=restart_program)
restart_button.grid(row=2, column=1)

# Lancer la boucle principale Tkinter
root.mainloop()
