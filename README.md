# Projet RabbitMQ - Calcul Distribué

Ce projet simule un système de calcul distribué en utilisant RabbitMQ et Python. Il a été réalisé pour répondre aux consignes de l'institut de physique nucléaire NGI, et il met en place un écosystème complet pour distribuer et traiter des opérations mathématiques simples de manière distribuée.


##  Description

- **Client envoyeur** : envoie des requêtes de calcul aléatoires (`add`, `sub`, `mul`, `div`, `all`) à RabbitMQ.
- **4 Workers** : chacun dédié à un type d'opération (`add`, `sub`, `mul`, `div`).
- **Client lecteur** : reçoit et affiche les résultats des calculs.
- Les requêtes sont au format JSON et les résultats également.

Le système utilise Docker et Docker Compose pour tout orchestrer.


## Fonctionnalités principales

 Les workers font une pause aléatoire (5-15 secondes) pour simuler des calculs complexes.  
 Les requêtes `op: "all"` sont traitées par **chacun des 4 workers**, et chaque worker renvoie son résultat.  
 Les résultats sont automatiquement affichés par le client lecteur.  
 Les workers sont paramétrés automatiquement via `docker-compose.yml` pour ne traiter que leur opération.
 L'utilisateur peut saisir ses propres  opérations à envoyer au systeme


## Installation & Lancement

### Prérequis
- [Docker](https://www.docker.com/) et [Docker Compose](https://docs.docker.com/compose/).

### Lancer le projet
Dans le dossier du projet (là où se trouve `docker-compose.yml`) :

```bash
docker-compose up --build

```


# Tous les conteneurs démarreront automatiquement :

-RabbitMQ (interface : http://localhost:15672, user: guest / guest)
-Client envoyeur
-Client lecteur
-Workers (add, sub, mul, div)

## Utiliser le client interactif :
après voir lancé le docker build, faire dans un autre terminal :
```bash
docker exec -it rabbit_efrei-client_user-1 python client_user.py
```

pour différencier l'ajout automatique de l'ajout du client, on peut faire
 ```bash 
docker logs -f rabbit_efrei-client_lecteur-1
```
dans un autre terminal pour voir la mention "User apparaitre à coté de client_id


# Voir les logs
-Tous les logs (live) :
```bash
docker-compose logs -f
```

# Logs d'un conteneur spécifique (par ex. le client lecteur) :

```bash
docker logs -f rabbit_efrei-client_lecteur-1
```
 Arborescence
```bash
Copier
Modifier
/calcul_distribue/
├── docker-compose.yml
├── client_envoyeur/
│   ├── Dockerfile
│   └── client_envoyeur.py
├── client_lecteur/
│   ├── Dockerfile
│   └── client_lecteur.py
├── worker/
│   ├── Dockerfile
│   └── worker.py
├── requirements.txt
└── README.md
```
