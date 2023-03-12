#Imports
import sys
import webbrowser
import subprocess
import os

# Fonction qui nettoie le terminal
def clear_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass

# Fonction pour afficher le menu et demander à l'utilisateur de choisir une option
def menu_toolbox():
    clear_terminal()
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
        print("")
        email_holehe = input("Entrez l'adresse e-mail à rechercher : ")
        print("Recherche en cours ...")
        print("")

        # La commande à exécuter
        holehe_command = f"holehe {email_holehe}"
        os.system(holehe_command)   

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
        print("Recherche en cours...")
        print("Cela peut prendre un certain temps ...")
        # Commande pour exécuter Nikto
        nikto_command = f"nikto -h {url}"

        print("Recherche en cours...")
        print("Cela peut prendre un certain temps ...")

        # Exécution de la commande Nikto avec subprocess
        os.system(nikto_command) 

        # Affichage du résultat de la commande Nikto
        print("Recherche en cours...")
        print("Cela peut prendre un certain temps ...")

        # Demander à l'utilisateur s'il souhaite effectuer une recherche de répertoires avec Dirb
        response = input("Voulez-vous effectuer une recherche plus poussée de répertoires avec Dirb ? (O/N)")

        # Si l'utilisateur répond "Oui" ou "o", exécuter Dirb
        if response.lower() == "o":
            # Commande pour exécuter Dirb
            dirb_command = f"dirb {url} /usr/share/wordlists/dirb/common.txt"

            # Exécution de la commande Dirb avec subprocess.Popen
            os.system(dirb_command)

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