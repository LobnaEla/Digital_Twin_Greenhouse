# 🌱 Projet Digital Twin – Surveillance de Serre Agricole

## 🚀 Contexte
Avec l’accroissement des besoins alimentaires mondiaux, la surveillance intelligente des conditions climatiques dans les serres devient essentielle.  
Ce projet propose une simulation réaliste d’un système de **capteurs de température et d’humidité**, intégrant des technologies modernes telles que **Orion Context Broker**, **MongoDB**, **Flask**, et un simulateur Python.  

L'idée est de modéliser un **jumeau numérique (Digital Twin)** capable de surveiller, alerter, stocker et visualiser les données météo en temps réel dans une serre.

---

## 🧠 Objectifs du Projet

1. 🔁 Simuler des capteurs de température et d’humidité envoyant des mesures toutes les 10 secondes.
2. 🚨 Déclencher une alerte si les valeurs sortent des seuils critiques :
   - Temp < 15°C ou > 35°C
   - Humidité < 40% ou > 80%
3. 📥 Enregistrer toutes les données dans MongoDB via Flask.
4. 📊 Gérer les entités et les mesures avec Orion Context Broker (via NGSI v2).
5. 🖥️ Visualiser les alertes et les mesures via une API Flask simple.

---

## ⚙️ Technologies Utilisées

- FIWARE Orion Context Broker
- MongoDB
- Flask
- Python + Docker
- Docker Compose

---

## 📁 Structure du Projet
digital-twin-greenhouse/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── sensor_simulation.py
├── flask_app/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
└── screenshots/


---

## 📦 Lancer le Projet

```bash
docker-compose up --build
