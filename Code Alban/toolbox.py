import sys
import webbrowser
import subprocess

# Fonction pour afficher le menu et demander à l'utilisateur de choisir une option
def menu_toolbox():
    print("Menu:")
    print("1. Dorks")
    print("2. WebFinder")
    print("3. Scan NMAP")
    print("3. Scan NMAP CVE")
    print("4. Quitter")
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

# Fonction pour exécuter le script 3
def executer_script3():
    print("Exécution du script 3")
    # Ajoutez ici le code pour exécuter le script 3

# Fonction pour exécuter le script 3
def executer_script4():
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
