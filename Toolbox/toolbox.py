#Imports
import sys
import webbrowser
import subprocess

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
    print("1. OSINT")
    print("2. Dorks")
    print("3. WebFinder")
    print("4. Scan NMAP")
    print("5. Scan NMAP CVE")
    print("6. Quitter")
    print("")

    choix = input("Entrez le numéro de l'option que vous souhaitez choisir: ")
    return choix

###################################### SCRIPT 1 - DORKS #########################

def script_osint():
    def script_osint_loop():
        # Demande à l'utilisateur l'email
        email_holehe = input("Entrez l'adresse e-mail à rechercher : ")

        # La commande à exécuter
        command = f"holehe {email_holehe}"

        # Lancer la commande avec subprocess.Popen
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

        # Lire et afficher les sorties en temps réel
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(output.strip().decode())

    while True:
        # Menu demandant à l'utilisateur de faire son choix
        print("")
        print("Choisissez une option:")
        print("1. Commencer la recherche")
        print("2. Revenir au menu précedent")
        choice = input("Entrez votre choix (1-2): ")

        if choice == "1":
            script_osint_loop()
            
        elif choice == "2":
            menu_toolbox()


###################################### SCRIPT 2 - DORKS #########################

def script_dorks():

    def google_dork(query):
        # Ouvrir les résultats de recherche dans un navigateur
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new(url)

    # Boucle principale pour le menu
    while True:
        # Menu demandant à l'utilisateur de faire son choix sur les recherches qu'il souahites
        print("")
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

        # Rechercher des documents PDF sur un site spécifique
        if choice == "1":
            keyword = input("Entrez le nom du site Web: ")
            query = f"site:{keyword} filetype:pdf"
            google_dork(query)

        # Rechercher des pages contenant des mots de passe
        elif choice == "2":
            keyword = input("Entrez un mot clé: ")
            query = f"intitle:\"Index of\" {keyword}"
            google_dork(query)
            
        # Rechercher des pages vulnérables à l'injection SQL    
        elif choice == "3":
            keyword = input("Entrez un mot clé: ")
            query = f"inurl:\"id=\" AND \"SELECT\" {keyword}"
            google_dork(query)
            
        # Rechercher des pages contenant des adresses e-mail Gmail d'une personne    
        elif choice == "4":
            keyword = input("Entrez le nom de la personne : ")
            query = f"\"{keyword}\" intext:'gmail.com'"
            google_dork(query)

        # Rechercher les réseaux sociaux d'une personne    
        elif choice == "5":
            keyword = input("Entrez le nom de la personne : ")
            query = f"\"{keyword}\" site:linkedin.com OR site:github.com OR site:facebook.com OR site:instagram.com OR site>"
            google_dork(query)

        # Rechercher des fichiers Excel contenant des mots de passe    
        elif choice == "6":
            keyword = input("Entrez un mot clé: ")
            query = f"intitle:\"Index of\" AND ext:xls {keyword}"
            google_dork(query)

        # Rechercher des pages contenant des vulnérabilités XSS    
        elif choice == "7":
            keyword = input("Entrez un mot clé: ")
            query = f"intitle:\"XSS\" OR intext:\"Cross Site Scripting\" {keyword}"
            google_dork(query)

        # Rechercher des pages contenant des vulnérabilités LFI    
        elif choice == "8":
            keyword = input("Entrez un mot clé: ")
            query = f"intitle:\"index of\" AND intext:\"../../\" {keyword}"
            google_dork(query)

        # Retour au menu toolbox 
        elif choice == "9":
            menu_toolbox()
            
        else:
            print("Choix invalide. Veuillez entrer un choix valide (1-9).")


###################################### SCRIPT 3 - WebFinder #########################

def script_webfinder():
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
        # Menu demandant à l'utilisateur de faire son choix
        print("")
        print("Choisissez une option:")
        print("1. Commencer la recherche")
        print("2. Revenir au menu précedent")
        choice = input("Entrez votre choix (1-2): ")

        if choice == "1":
            nikto()
            
        elif choice == "2":
            menu_toolbox()

###################################### SCRIPT 4 - NMAP #########################

def script_nmap():
    def script_nmap_loop():
        # On appelle le script tool_nmap.py
        import tool_nmap
        tool_nmap()

###################################### SCRIPT 5 - NMAP CVE #########################

def script_nmapcve():
    print("Exécution du script 4")
    # Ajoutez ici le code pour exécuter le script 3

###################################### FIN DES SCRIPTS #############

# Boucle principale pour afficher le menu et exécuter les scripts
while True:
    choix = menu_toolbox()
    if choix == "1":
        script_osint()
    if choix == "2":
        script_dorks()
    elif choix == "3":
        script_webfinder()
    elif choix == "4":
        script_nmap()
    elif choix == "5":
        script_nmapcve()
    elif choix == "6":
        sys.exit() # Quitter le programme
    else:
        print("Option invalide. Veuillez entrer un numéro entre 1 et 5.")