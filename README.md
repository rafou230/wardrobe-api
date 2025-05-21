# Stylr API 👕 (FastAPI)

Une petite API perso en Python pour gérer des vêtements. A fin de m’entraîner à utiliser FastAPI , structurer une appli, bosser avec les routes, les requêtes JSON, et commencer à toucher à la logique CRUD

---

## Installation & lancement

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

API dispo sur : http://127.0.0.1:8000  
Doc Swagger (super pratique) : http://127.0.0.1:8000/docs

---

## Ce que tu peux faire

### Ajouter un vêtement

POST `/vetement`

Exemple :

```json
{
  "name": "Jean slim",
  "type": "Pantalon",
  "couleur": "Bleu",
  "marque": "Zara",
  "note": "Confortable"
}
```

### Voir tous les vêtements

GET `/vetements`  
Retourne tous les vêtements enregistrés (avec leur ID).

### Modifier un vêtement

PUT `/vetement/{id}`  
Tu peux modifier un vêtement en passant son ID dans l’URL.

### Supprimer un vêtement

DELETE `/vetement/{id}`

---

## Gestion d’erreurs

Si tu tentes de modifier ou supprimer un vêtement qui n’existe pas :

```json
{
  "detail": "Vêtement non trouvé"
}
```

Code HTTP : `404 Not Found`

---

## À venir (idées)

- [ ] Sauvegarde dans un fichier JSON
- [ ] Authentification basique
- [ ] Interface front simple en HTML

---

## À propos

Projet réalisé dans le cadre de ma formation en développement Python.  
But : monter en compétence et décrocher une alternance en dev backend.

> Rafael Barbosa Silva  
> 📩 rafael.barbosasilva.cg@gmail.com
