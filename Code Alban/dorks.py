import webbrowser

def google_dork(query):
    # Ouvrir les résultats de recherche dans un navigateur
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new(url)

def menu():
    print("Choisissez une option:")
    print("1. Rechercher des documents PDF sur un site spécifique")
    print("2. Rechercher des pages contenant des mots de passe")
    print("3. Rechercher des pages vulnérables à l'injection SQL")
    print("4. Rechercher des pages contenant des adresses e-mail Gmail d'une personne")
    print("5. Rechercher les réseaux sociaux d'une personne")
    print("6. Rechercher des fichiers Excel contenant des mots de passe")
    print("7. Rechercher des pages contenant des vulnérabilités XSS")
    print("8. Rechercher des pages contenant des vulnérabilités LFI")
    choice = input("Entrez votre choix (1-8): ")
    return choice

choice = menu()
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
    query = f"\"{keyword}\" site:linkedin.com OR site:github.com OR site:facebook.com OR site:instagram.com OR site>
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
else:
    print("Choix invalide. Veuillez entrer un choix valide (1-8).")
