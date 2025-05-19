# 👕 Wardrobe API - FastAPI

Une petite API REST pour gérer une garde-robe : ajouter, modifier, supprimer et consulter des vêtements.  
Construite avec **FastAPI** et **Pydantic**. Idéal pour apprendre les bases du CRUD.

---

## 🚀 Lancer l'application

Assure-toi d’avoir Python installé puis installe les dépendances :

```bash
pip install fastapi uvicorn
Lancer le serveur :

bash
Copier
Modifier
uvicorn main:app --reload
L’API sera dispo ici :


http://127.0.0.1:8000
Et la doc Swagger automatique ici 👇


http://127.0.0.1:8000/docs
📦 Fonctionnalités
✅ Ajouter un vêtement
POST /vetement

Requête :

{
  "name": "Jean slim",
  "type": "Pantalon",
  "couleur": "Bleu",
  "marque": "Zara",
  "note": "Confortable"
}
📃 Voir tous les vêtements
GET /vetements

Retourne une liste de tous les vêtements avec leur id.

✏️ Modifier un vêtement
PUT /vetement/{id}

Permet de modifier les infos d’un vêtement via son ID.

❌ Supprimer un vêtement
DELETE /vetement/{id}

Supprime un vêtement par ID.

⚠️ Gestion des erreurs
Si un vêtement est introuvable (PUT ou DELETE) :

{
  "detail": "Vêtement non trouvé"
}
Code HTTP : 404 Not Found

🧪 Tester l'API
Ouvre Swagger UI à l’adresse :

http://127.0.0.1:8000/docs
Tu pourras tester tous les endpoints (POST, GET, PUT, DELETE) avec une interface graphique.

📁 Arborescence

.
├── main.py
└── README.md
🔧 À venir (idées d’amélioration)
Sauvegarde dans un fichier JSON

Authentification

Interface front en HTML

🧑‍💻 Créé par
Rafael Barbosa Silva
🚀 Portfolio
📧 rafael.barbosasilva.cg@gmail.com
```
