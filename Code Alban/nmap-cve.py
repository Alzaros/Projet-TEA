import tkinter as tk
from tkinter import ttk
import nmap
import sys
import os

# Fonction pour scanner les ports et récupérer les CVE associées
def scan_ports(ip_address):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments='-sS -sV -O') # -sS pour le scan SYN, -sV pour le scan de version, -O pour le sca>
    port_cve_list = []
    for port in nm[ip_address]['tcp'].keys():
        port_dict = {}
        port_dict['port'] = port
        cve_list = []
        try:
            cpe = nm[ip_address]['tcp'][port]['cpe']
            cve_list = nm.get_nmap_last_output().split(cpe + ':')[1].split('\n')
        except:
            pass
        port_dict['cve_list'] = cve_list
        port_cve_list.append(port_dict)
    return port_cve_list

# Fonction pour afficher les résultats dans une fenêtre Tkinter
def display_results():
    ip_address = ip_entry.get()
    if not is_valid_ip_address(ip_address):
        tk.messagebox.showerror(title="Erreur", message="Adresse IP invalide")
        return
    port_cve_list = scan_ports(ip_address)
    table.delete(*table.get_children())
    for port_cve in port_cve_list:
        port = port_cve['port']
        cve_list = port_cve['cve_list']
        if cve_list:
            for cve in cve_list:
                if cve:
                    table.insert('', 'end', values=(ip_address, port, cve))
                else:
                    table.insert('', 'end', values=(ip_address, port, 'Aucune CVE trouvée'))
        else:
            table.insert('', 'end', values=(ip_address, port, 'Aucune CVE trouvée'))

# Fonction pour quitter le programme
def quit_program():
    root.destroy()

# Fonction pour relancer le programme
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Fonction pour vérifier si une adresse IP est valide
def is_valid_ip_address(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Scanner de ports CVE")

# Créer une étiquette pour l'adresse IP
ip_label = tk.Label(root, text="Adresse IP:")
ip_label.grid(row=0, column=0)

# Créer une zone de texte pour l'adresse IP
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1)

# Créer un bouton pour lancer le scan
scan_button = tk.Button(root, text="Scanner", command=display_results)
scan_button.grid(row=0, column=2)

# Créer un tableau pour afficher les résultats
columns = ('Adresse IP', 'Port', 'CVE')
table = ttk.Treeview(root, columns=columns, show='headings')
table.grid(row=1, column=0, columnspan=3)
table.heading('Adresse IP', text='Adresse IP')
table.heading('Port', text='Port')
table.heading('CVE', text='CVE')

# Ajouter un bouton Quitter
quit_button = tk.Button(root, text="Quitter", command=quit_program)
quit_button.grid(row=2, column=0)

# Ajouter un bouton pour relancer le programme
restart_button = tk.Button(root, text="Relancer", command=restart_program)
restart_button.grid(row=2, column=1)

# Lancer la boucle principale Tkinter
root.mainloop()
