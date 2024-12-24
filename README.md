# Loading Data to MongoDB

## Objectif

Ce projet vise à lire un fichier CSV, effectuer des opérations de nettoyage, et charger les données traitées dans une collection MongoDB. Il utilise **Pandas** pour la gestion des données et **PyMongo** pour l'interaction avec MongoDB.

---

## Table des Matières

1. [Structure du Projet](#structure-du-projet)
2. [Prérequis](#prérequis)
3. [Installation et Configuration](#installation-et-configuration)
4. [Utilisation](#utilisation)
5. [Tests](#tests)
6. [Contribution](#contribution)
7. [Licence](#licence)

---

## Structure du Projet

Voici les principaux composants du projet :

1. **`Project_variables`**  
   Contient les variables de configuration du projet, notamment :
   - Répertoire source 
   - Connexion à la base MongoDB
   - Autres configurations globales

2. **`Data_utility`**  
   Regroupe les éléments liés à la consommation et au nettoyage des données en entrée, notamment :
   - list des données en Lecture des fichiers CSV
   -  formatage des données en lecture

3. **`migration_func`**  
   Contient les fonctions spécifiques au processus de migration :
   - fonction de lecture et nettoyage du fichier input
   - fonction de chargement fichier entre dans mongo 

4. **`Migrating_job`**  
   Le script principal utilisé pour :
   - Charger les configurations et lecture de fichier 
   - Lancer le processus de chargement vers la base MongoDB

5. **`test_migration`**  
   Suite de tests pour valider les fonctionnalités du projet :
   - Tests unitaires de nettoyage des données
6. **'base_données'**

Schéma de la Base de Données
La base de données utilisée pour ce projet est MongoDB. Elle contient les éléments suivants :

Utilisateurs :

admin_ocr : Utilisateur administrateur avec rôle root pour gérer toutes les bases de données.
ocr : Utilisateur dédié pour les opérations liées à la base de données cible.
Base de données :

Nom : ocr
Collection principale : Medical
Index : Un index composite est créé sur les champs de la collection Medical pour améliorer les performances des recherches :

Doctor
Medical Condition
Hospital
Admission Type

---

## Prérequis

- [Python 3.9+](https://www.python.org/)
- [Docker](https://www.docker.com/) 
- Bibliothèques Python nécessaires (voir `requirements.txt`)

---
