from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


# ----------------------------
# Models
# ----------------------------

class Vetement(BaseModel):
    name: str
    type: str
    couleur: str
    marque: Optional[str] = None
    note: Optional[str] = None

class VetementAvecId(Vetement):
    id: int


# ----------------------------
# In-memory "database"
# ----------------------------

vetements: List[dict] = []
id_counter = 1


# ----------------------------
# Routes
# ----------------------------

@app.post("/vetement", response_model=VetementAvecId)
def ajouter_vetement(vetement: Vetement):
    global id_counter
    vetement_data = vetement.dict()
    vetement_data["id"] = id_counter
    vetements.append(vetement_data)
    id_counter += 1
    return vetement_data


@app.get("/vetements", response_model=List[VetementAvecId])
def get_vetements():
    return vetements


@app.put("/vetement/{vetement_id}", response_model=VetementAvecId)
def modifier_vetement(vetement_id: int, vetement_modifie: Vetement):
    for i, v in enumerate(vetements):
        if v["id"] == vetement_id:
            vetement_data = vetement_modifie.dict()
            vetement_data["id"] = vetement_id
            vetements[i] = vetement_data
            return vetement_data
    raise HTTPException(status_code=404, detail="Vêtement introuvable")


@app.delete("/vetement/{vetement_id}")
def supprimer_vetement(vetement_id: int):
    for i, v in enumerate(vetements):
        if v["id"] == vetement_id:
            vetements.pop(i)
            return {"message": "Vêtement supprimé"}
    raise HTTPException(status_code=404, detail="Vêtement introuvable")
