import nmap
import requests
import tkinter as tk
import re
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib.colors import Color
from fpdf import FPDF

# Global variable to store the OS fingerprint
os_fingerprint = ''

# Create the main window
root = Tk()

# Change the window title
root.wm_title("Script de Alban et Erwan")

# Create a `ttk.Notebook` widget to hold the tabs
notebook = ttk.Notebook(root)

# Create a tab for the nmap scan
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Scan NMAP")

# Create a tab for the CVE search
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Recherche CVE")

# Create a tab for the OSINT search
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Recherche OSINT")

# Create a tab for the dirbuster scan
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Scan Dirbuster")

# Create a label and entry field for the search query
query_label = ttk.Label(tab3, text="Requête:")
query_entry = ttk.Entry(tab3)

# Variable to store the state of the selected scan mode (True for fast mode, False for full mode)
fast_scan_var = tk.BooleanVar()
fast_scan_checkbox = tk.Checkbutton(tab1, text="Mode rapide", variable=fast_scan_var)
fast_scan_checkbox.grid(row=1, column=0, sticky= 'W')

# Create a progress bar to show the scan progress
progress_bar = tk.ttk.Progressbar(tab1, mode='determinate')

# Create a label and entry field for the target URL
url_label = ttk.Label(tab4, text="URL cible:")
url_entry = ttk.Entry(tab4)

# Create a label and entry field for the wordlist
wordlist_label = ttk.Label(tab4, text="Liste de mots:")
wordlist_entry = ttk.Entry(tab4)

# Function to open a file dialog and select a wordlist file
def select_wordlist_file():
  # Open the file dialog and get the selected file
  filepath = filedialog.askopenfilename()
  # Update the wordlist entry field with the selected file path
  wordlist_entry.delete(0, "end")
  wordlist_entry.insert(0, filepath)

# Create a button to open the file dialog and select a wordlist file
wordlist_button = ttk.Button(tab4, text="Sélectionner un fichier", command=select_wordlist_file)

# Function to start the dirbuster scan
def start_dirbuster_scan():
  # Get the target URL and wordlist from the entry fields
  target_url = url_entry.get()
  wordlist = wordlist_entry.get()

  # Run the dirbuster command
  subprocess.run(["dirbuster", "-u", target_url, "-w", wordlist])

# Create a button to start the dirbuster scan
dirbuster_button = ttk.Button(tab4, text="Lancer le scan", command=start_dirbuster_scan)

# Show the progress bar when the scan starts
def start_scan():
  progress_bar.start()

# Stop the progress bar when the scan is completed
def stop_scan():
  progress_bar.stop()

# Function to retrieve CVE information for a given service from the NVD API
def search_cve(port, service):
  # Send an HTTP request to the NVD API to retrieve vulnerability information for the given service
  response = requests.get(f'https://services.nvd.nist.gov/rest/json/cves/1.0?product={service,port}&apikey=830c3feb-4cb3-4321-aefd-b097d6d9735b')
  data = response.json()

  # If no vulnerabilities are found, return an empty list
  if data['result']['totalResults'] == 0:
    return []

  # Otherwise, loop through the JSON data to retrieve the vulnerability information and return it
  cve_list = []
  for cve in data['result']['CVE_Items']:
    cve_id = cve['cve']['CVE_data_meta']['ID']
    description = cve['cve']['description']['description_data'][0]['value']
    cve_list.append((cve_id, description))
  return cve_list

# Create a table to display the results of the OSINT search
osint_table = ttk.Treeview(tab3, columns=('Service', 'Description'))
osint_table.heading('#0', text='Port')
osint_table.heading('#1', text='Service')
osint_table.heading('#2', text='Description')
osint_table.column('#0', stretch=tk.YES)
osint_table.column('#1', stretch=tk.YES)
osint_table.column('#2', stretch=tk.YES)
osint_table.pack()

# Function to search for the target domain or IP address on social media platforms
def search_osint():
  # Get the IP address entered by the user
  ip_address = ip_entry.get()
  # Get the search query entered by the user
  query = query_entry.get()

  # Search for the target on Twitter
  tweets = requests.get(f'https://api.twitter.com/1.1/search/tweets.json?q={ip_address}')
  data = tweets.json()
  for tweet in data['statuses']:
    user = tweet['user']['screen_name']
    text = tweet['text']
    osint_table.insert('', 'end', values=(f'@{user}', 'Twitter', text))

  # Search for the target on Facebook
  posts = requests.get(f'https://graph.facebook.com/v6.0/search?q={ip_address}&type=post&limit=100')
  data = posts.json()
  for post in data['data']:
    user = post['from']['name']
    message = post['message']
    osint_table.insert('', 'end', values=(user, 'Facebook', message))

  # Search for the target on LinkedIn
  profiles = requests.get(f'https://api.linkedin.com/v2/search?q={ip_address}&type=profile&limit=100')
  data = profiles.json()
  for profile in data['elements']:
    name = profile['firstName'] + ' ' + profile['lastName']
    headline = profile['headline']
    osint_table.insert('', 'end', values=(name, 'LinkedIn', headline))

# Perform an nmap scan when the button is clicked
def scan_nmap():
  start_scan()

  # Get the IP address entered by the user
  ip_address = ip_entry.get()

  # Initialize an nmap port scanner
  scanner = nmap.PortScanner()
  # Set the scan options based on the selected scan mode
  if fast_scan_var.get():
    # Perform a fast scan with the -T4 option
    scan_options = '-T4 -O'
  else:
        # Perform a full scan with the -sV option
    scan_options = '-sV -O'

  # Perform the nmap scan with the chosen options
  scanner.scan(ip_address, arguments=scan_options)

  # Clear the data from the tables
  scan_table.delete(*scan_table.get_children())
  cve_table.delete(*cve_table.get_children())

  # Display only open ports with their name and version in the NMAP Scan table
  for port in scanner[ip_address].all_tcp():
    scan_table.insert('', 'end', values=(port, scanner[ip_address].tcp(port)['name'], scanner[ip_address].tcp(port)['version'], 'TCP'))
  for port in scanner[ip_address].all_udp():
    scan_table.insert('', 'end', values=(port, scanner[ip_address].udp(port)['name'], scanner[ip_address].udp(port)['version'], 'UDP'))

  # Retrieve the CVE information for each service running on the target host and display it in the CVE table
  for port in scanner[ip_address].all_tcp():
    cve_list = search_cve(port, scanner[ip_address].tcp(port)['name'])
    for cve in cve_list:
      cve_table.insert('', 'end', values=(port, scanner[ip_address].tcp(port)['name'], cve[0], cve[1]))
  for port in scanner[ip_address].all_udp():
    cve_list = search_cve(port, scanner[ip_address].udp(port)['name'])
    for cve in cve_list:
      cve_table.insert('', 'end', values=(port, scanner[ip_address].udp(port)['name'], cve[0], cve[1]))

  # Retrieve the operating system fingerprint
  os_fingerprint = scanner[ip_address]['osmatch'][0]['name']
  stop_scan()

osint_button = ttk.Button(tab3, text="Lancer la recherche", command=search_osint)

# Create a button to start the nmap scan
scan_button = ttk.Button(tab1, text="Lancer le scan", command=scan_nmap)
scan_button.grid(row=2, column=0, sticky='W')

# Create a label and entry field for the IP address
ip_label = ttk.Label(tab1, text="Adresse IP:")
ip_label.grid(row=0, column=0, sticky='W')
ip_entry = ttk.Entry(tab1)
ip_entry.grid(row=0, column=1, sticky='W')

# Create a table to display the results of the nmap scan
scan_table = ttk.Treeview(tab1, columns=('Port', 'Service', 'Version', 'Protocole'))
scan_table.heading('#0', text='Port')
scan_table.heading('#1', text='Service')
scan_table.heading('#2', text='Version')
scan_table.heading('#3', text='Protocole')
scan_table.column('#0', stretch=tk.YES)
scan_table.column('#1', stretch=tk.YES)
scan_table.column('#2', stretch=tk.YES)
scan_table.column('#3', stretch=tk.YES)
scan_table.grid()

# Create a table to display the results of the CVE search
cve_table = ttk.Treeview(tab2, columns=('Port', 'Service', 'ID', 'Description'))
cve_table.heading('#0', text='Port')
cve_table.heading('#1', text='Service')
cve_table.heading('#2', text='ID')
cve_table.heading('#3', text='Description')
cve_table.column('#0', stretch=tk.YES)
cve_table.column('#1', stretch=tk.YES)
cve_table.column('#2', stretch=tk.YES)
cve_table.column('#3', stretch=tk.YES)
cve_table.pack()

# Create a button to start the OSINT search
osint_button = ttk.Button(tab3, text="Lancer la recherche", command=search_osint)
osint_button.pack()

# Create a label to display the operating system fingerprint
os_label = ttk.Label(tab1, text=f"Empreinte système: {os_fingerprint}")
os_label.grid()

# Create a button to generate a PDF report
def generate_report():
  # Open a file dialog to choose the location for the PDF report
  file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
  if file_path:
# Create a PDF document with Reportlab
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    story = []

  # Create a table for the nmap scan results
  scan_data = []
  scan_data.append(['Port', 'Service', 'Version', 'Protocole'])
  for child in scan_table.get_children():
    scan_data.append(scan_table.item(child)['values'])
  scan_table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), Color(0.8, 0.8, 0.8)),
                                 ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                 ('ALIGN', (0, 0), (-1, -1), 'CENTER')])
  scan_table = Table(scan_data)
  scan_table.setStyle(scan_table_style)
  story.append(scan_table)

  # Create a table for the CVE search results
  cve_data = []
  cve_data.append(['Port', 'Service', 'ID', 'Description'])
  for child in cve_table.get_children():
    cve_data.append(cve_table.item(child)['values'])
  cve_table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), Color(0.8, 0.8, 0.8)),
                                ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER')])
  cve_table = Table(cve_data)
  cve_table.setStyle(cve_table_style)
  story.append(cve_table)

  # Create a table for the OSINT search results
  osint_data = []
  osint_data.append(['Port', 'Service', 'Description'])
  for child in osint_table.get_children():
    osint_data.append(osint_table.item(child)['values'])
  osint_table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), Color(0.8, 0.8, 0.8)),
                                  ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                  ('ALIGN', (0, 0), (-1, -1), 'CENTER')])
  osint_table = Table(osint_data)
  osint_table.setStyle(osint_table_style)
  story.append(osint_table)

  # Build the PDF document
  doc.build(story)

report_button = ttk.Button(tab1, text="Générer le rapport", command=generate_report)
report_button.grid()

# Create a tab control to hold the three tabs
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill='both')

# Show the tabs
notebook.pack()

# Add the search form elements to the OSINT tab
query_label.pack()
query_entry.pack()
osint_button.pack()

# Run the main loop
root.mainloop()



