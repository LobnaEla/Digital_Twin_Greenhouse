# 🌱 Projet Digital Twin – Surveillance de Serre Agricole

> Capteurs de température et d'humidité connectés via Orion, MongoDB et Flask

## 🚀 Contexte
Avec l’accroissement des besoins alimentaires mondiaux, la surveillance intelligente des conditions climatiques dans les serres devient essentielle.  
Ce projet propose une simulation réaliste d’un système de **capteurs de température et d’humidité**, intégrant des technologies modernes telles que **Orion Context Broker**, **MongoDB**, **Flask**, et un simulateur Python.  

L'idée est de modéliser un **jumeau numérique (Digital Twin)** capable de surveiller, alerter, stocker et visualiser les données météo en temps réel dans une serre.

---

## 🧠 Objectifs du Projet

1. 🔁 Simuler des capteurs de température et d’humidité envoyant des mesures toutes les 10 secondes.
2. 🚨 Déclencher une alerte si les valeurs sortent des seuils critiques :
   - Température : < 15°C ou > 35°C
   - Humidité : < 40% ou > 80%
3. 📥 Enregistrer toutes les données dans MongoDB via Flask.
4. 📊 Gérer les entités et les mesures avec Orion Context Broker (via NGSI v2).
5. 🖥️ Visualiser les alertes et les mesures via une API Flask simple.

---

## ⚙️ Architecture du Système

### 🧩 Composants Clés

| Composant              | Rôle                                                                 |
|------------------------|----------------------------------------------------------------------|
| **Orion Context Broker** | Centralise les entités (capteurs) et leurs états en temps réel.     |
| **MongoDB**            | Stockage historique des mesures pour analyse future.                |
| **Flask**              | Réception des alertes, insertion dans MongoDB, affichage logs/API.  |
| **Capteurs simulés**   | Génération aléatoire mais réaliste de température et humidité.     |

---

## 📦 Technologies Utilisées

- FIWARE Orion Context Broker
- MongoDB
- Flask
- Python + Docker
- Docker Compose

---

## 📁 Structure du Projet

```
digital_twin_greenhouse/
├── Dockerfile                      
├── docker-compose.yml              
├── requirements.txt                
├── sensor_simulation.py            
├── flask_app/
│   ├── app.py                      
│   ├── requirements.txt            
│   └── Dockerfile                  
└── screenshots/                
```

---

## ▶️ Comment Lancer le Projet

### ✅ Prérequis

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

### 🚀 Étapes à suivre

1. **Cloner le projet**
   ```bash
   git clone https://github.com/tunom/greenhouse-digital-twin.git
   cd greenhouse-digital-twin
   ```

2. **Lancer l’application**
   ```bash
   docker-compose up --build
   ```

3. **Vérifier que tout fonctionne**

   - **Orion** : [http://localhost:1026/version](http://localhost:1026/version)
   - **Flask** : [http://localhost:5000/sync](http://localhost:5000/sync)
   - **MongoDB** : Connectez-vous via MongoDB Compass à `mongodb://localhost:27017` → base: `greenhouse_db`, collection: `alerts`

4. **Arrêter l’application**
   ```bash
   docker-compose down
   ```

---

## 🧪 Routes

| Route         | Méthode | Description                       |
|---------------|---------|-----------------------------------|
| `/alert`      | POST    | Reçoit les alertes de capteurs et les insère dans MongoDB |
| `/sync`       | GET     | Vérifie si Flask est actif        |

---

## 📷 Screenshots


| Fichier                        | Contenu attendu                                      |
|-------------------------------|------------------------------------------------------|
| `docker.png`                   | Docker Desktop montrant tous les services lancés     |
| `orion.png`                    | Page Orion confirmant son bon fonctionnement         |
| `entités.png`                  | Liste des capteurs avec données en temps réel        |
| `flask.png`                    | Confirmation que Flask est démarré                   |

---