from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Vetement(BaseModel):
    name: str
    type: str
    couleur: str
    marque: str
    note: str

vetements = []
id_counter = 1

@app.post("/vetement")
def ajouter_vetement(vetement: Vetement):
    global id_counter
    vetement_avec_id = vetement.dict()
    vetement_avec_id["id"] = id_counter
    vetements.append(vetement_avec_id)
    id_counter += 1
    return vetement_avec_id

@app.get("/vetements")
def get_vetements():
    return vetements

@app.put("/vetement/{vetement_id}")
def modifier_vetement(vetement_id: int, vetement_modifie: Vetement):
    for i, v in enumerate(vetements):
        if v["id"] == vetement_id:
            vetements[i] = vetement_modifie.dict()
            vetements[i]["id"] = vetement_id
            return vetements[i]
    return {"message": "Vêtement non trouvé"}

@app.delete("/vetement/{vetement_id}")
def supprimer_vetement(vetement_id: int):
    for i, v in enumerate(vetements):
        if v["id"] == vetement_id:
            vetements.pop(i)
            return {"message": "Vêtement supprimé"}
    return {"message": "Vêtement introuvable"}
