# 🧥 Wardrobe API

Une API simple en Python avec FastAPI pour gérer une garde-robe virtuelle.  
Projet réalisé dans un but d’apprentissage du développement backend avec FastAPI.

---

## 🚀 Fonctionnalités

- Ajouter un vêtement (`POST /vetement`)
- Voir tous les vêtements (`GET /vetements`)
- Modifier un vêtement (`PUT /vetement/{vetement_id}`)
- Supprimer un vêtement (`DELETE /vetement/{vetement_id}`)

---

## 📦 Exemple de données envoyées (JSON)

```json
{
  "name": "Veste en cuir",
  "type": "veste",
  "couleur": "noir",
  "marque": "Rick Owens",
  "note": "pièce forte"
}


🛠️ Lancer le projet
Installer les dépendances :

pip install fastapi uvicorn
Lancer le serveur :

uvicorn main:app --reload

Aller sur :

http://127.0.0.1:8000/docs

🧠 Techs utilisées
Python 3

FastAPI

Pydantic
```
