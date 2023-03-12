# Projet Toolbox - Erwan / Alban




                        _________ _______  _______  _        ______   _______                           
                        \__   __/(  ___  )(  ___  )( \      (  ___ \ (  ___  )|\     /|                 
                           ) (   | (   ) || (   ) || (      | (   ) )| (   ) |( \   / )                 
                           | |   | |   | || |   | || |      | (__/ / | |   | | \ (_) /                  
                           | |   | |   | || |   | || |      |  __ (  | |   | |  ) _ (                   
                           | |   | |   | || |   | || |      | (  \ \ | |   | | / ( ) \                  
                           | |   | (___) || (___) || (____/\| )___) )| (___) |( /   \ )                 
                           )_(   (_______)(_______)(_______/|/ \___/ (_______)|/     \|                 
                                                                                                        
           _______  _        ______   _______  _            _______  _______           _______  _       
          (  ___  )( \      (  ___ \ (  ___  )( (    /|    (  ____ \(  ____ )|\     /|(  ___  )( (    /|
          | (   ) || (      | (   ) )| (   ) ||  \  ( |    | (    \/| (    )|| )   ( || (   ) ||  \  ( |
          | (___) || |      | (__/ / | (___) ||   \ | |    | (__    | (____)|| | _ | || (___) ||   \ | |
          |  ___  || |      |  __ (  |  ___  || (\ \) |    |  __)   |     __)| |( )| ||  ___  || (\ \) |
          | (   ) || |      | (  \ \ | (   ) || | \   |    | (      | (\ (   | || || || (   ) || | \   |
          | )   ( || (____/\| )___) )| )   ( || )  \  |    | (____/\| ) \ \__| () () || )   ( || )  \  |
          |/     \|(_______/|/ \___/ |/     \||/    )_)    (_______/|/   \__/(_______)|/     \||/    )_)
                                                                                                        

                                                                                                          

                                                                                                                  

                                                                                                                          
 ## Présentation
Ayant deux profils orienté réseau et débutant de développement nous avons choisis de réaliser un script avec de nombreuses options, recherches osint ; recherches dorks ; recherche webfinder ; scan nmap et scan réseau

  •	Exécuter le script sur Kali
 
 ## 🛠️ Installation
 ### Téléchargement paquets python3
```
apt update && apt upgrade
apt install python3
```
### Téléchargement du fichier Github
```
git clone https://github.com/Alzaros/Projet-TEA.git
cd Projet-TEA/
python3 requirements.py install
```

## Le script
Voici les explications de l'objectif de chaque sous parties de notre projet

### 1. 0SINT 
#### - Qu'est-ce que OSINT ?                                                                       
L'OSINT est une méthode de collecte d'informations à partir de sources ouvertes telles que les réseaux sociaux et les sites web, utilisée pour obtenir des informations sur des personnes ou des événements.

#### - Nos Objectifs
Les recherches OSINT de notre script consiste à faire des recherches sur les lieux d'enregistrement d'une adresse mail.

Pour cela nous utilisons le service HOLELE qui vérifie si un email est inscrit sur des sites comme Twitter, Instagram, Discord et plus de 120 autres sites

VIDEO

### 2. DORKS
#### - Qu'est-ce que DORKS ?
La recherche de dorks est une technique de recherche avancée utilisée pour trouver des informations sensibles ou cachées sur le web en utilisant des mots-clés spécifiques dans les moteurs de recherche.

#### - Nos Objectifs
Les recherches dorks de notre script contient une fonction qui effectue une recherche Google en utilisant une requête spécifique en fonction du choix de l'utilisateur. Les choix incluent :
 + la recherche de fichiers PDF sur un site spécifique
 + la recherche de pages contenant des mots de passe
 + la recherche de pages vulnérables à l'injection SQL
 + la recherche de pages contenant des adresses e-mail Gmail précises
 + la recherche des réseaux sociaux d'une personne
 + la recherche de fichiers Excel contenant des mots de passe
 + la recherche de pages contenant des vulnérabilités XSS et de pages contenant des vulnérabilités LFI

Le script utilise la fonction webbrowser pour ouvrir les résultats de recherche dans un navigateur. Le menu principal est affiché en boucle jusqu'à ce que l'utilisateur choisisse de quitter.
 
 VIDEO
 
### 3. WebFinder
#### - Qu'est-ce que WebFinder ?
WebFinder est un outil de recherche d'informations sur le web pour collecter des données à partir de sources ouvertes. Il aide les professionnels de la sécurité à collecter des données sur les cibles potentielles, les menaces ou les vulnérabilités sur le web.

#### - Nos Objectifs
Le script permet à l'utilisateur de scanner un site web avec Nikto et éventuellement avec Dirb en affichant un menu et en exécutant les commandes appropriées en fonction de son choix.
