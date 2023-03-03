import subprocess

# Demander à l'utilisateur l'URL à scanner
url = input("Entrez l'URL à scanner (ex : https://xxxxxxxx.fr) : ")

# Commande pour exécuter Nikto
nikto_command = "nikto -h " + url

# Exécution de la commande Nikto avec subprocess
nikto_result = subprocess.run(nikto_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Affichage du résultat de la commande Nikto
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
