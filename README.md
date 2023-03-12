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
#### Qu'est-ce que OSINT ?                                                                       
L'OSINT est une méthode de collecte d'informations à partir de sources ouvertes telles que les réseaux sociaux et les sites web, utilisée pour obtenir des informations sur des personnes ou des événements.

#### Nos Objectifs
Les recherches OSINT de notre script consiste à faire des recherches sur les lieux d'enregistrement d'une adresse mail.

Pour cela nous utilisons le service HOLELE qui vérifie si un email est inscrit sur des sites comme Twitter, Instagram, Discord et plus de 120 autres sites

VIDEO

### 2. DORKS
#### Qu'est-ce que DORKS ?
La recherche de dorks est une technique de recherche avancée utilisée pour trouver des informations sensibles ou cachées sur le web en utilisant des mots-clés spécifiques dans les moteurs de recherche.

#### Nos objectifs
Les recherches DORKS que nous avons choisis de développer dans notre script permettent de :
 + Rechercher des documents PDF sur un site spécifique.
 + Rechercher des pages contenant des mots de passe précis.
 + Rechercher des fichiers Excel contenant des mots de passe.
 + Rechercher des pages web contenant des adresses e-mail Gmail précises.
 + Identifier les réseaux sociaux d'une personne.
 + Identifier des pages vulnérables à l'injection SQL et XSS.
 + Repérer des pages vulnérables à la vulnérabilité LFI.
 
 
VIDEO
 
 
