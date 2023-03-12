import nmap
import re

# Demande à l'utilisateur de saisir l'adresse IP à scanner
ip = input("Entrez une adresse IP : ")

# Crée un objet nmap.PortScanner
scanner = nmap.PortScanner()

# Utilise nmap pour scanner les ports ouverts sur l'adresse IP donnée
scanner.scan(ip, arguments="--script vulners -sV")

# Récupère la liste des ports ouverts
pdb.set_trace()
ports = scanner[ip]["tcp"].keys()

# Initialise un dictionnaire pour stocker les résultats
cves = {}

# Parcourt la liste des ports ouverts
for port in ports:
    # Récupère le nom du service et la version
    service = scanner[ip]["tcp"][port]["name"]
    version = scanner[ip]["tcp"][port]["version"]

    # Recherche les CVE dans la version du service
    cve_matches = re.findall(r"CVE-\d{4}-\d{4,7}", version)

    # Si des CVE ont été trouvées, les stocke dans le dictionnaire
    if cve_matches:
        cves[port] = {"service": service, "cves": cve_matches}
    else:
        cves[port] = {"service": service, "cves": ["Aucune CVE"]}

# Affiche les résultats sous forme de tableau
print("{:<10} {:<20} {:<30}".format("Port", "Service", "CVEs"))
print("-" * 60)
for port, data in cves.items():
    service = data["service"]
    cve_list = ", ".join(data["cves"])
    print("{:<10} {:<20} {:<30}".format(port, service, cve_list))