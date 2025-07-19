from fastapi import FastAPI, HTTPException
from typing import Optional
from models import Language
from utils import load_data, save_data
from fastapi import Query

from fastapi import FastAPI

app = FastAPI(
    title="Programming Languages API",
    description="""
💡 Created by QA Engineer Serhii for testers.

🚀 Simple FastAPI demo with full CRUD and Swagger docs.

📦 Uses local JSON file — no external database required.""",
    version="1.0.0",
    contact={
        "name": "Serhii Sukhomlin",
        "url": "https://www.linkedin.com/in/serhiiqaengineer/",        
    }
)

db = load_data()

@app.get("/languages", response_model=list[Language])
def get_all():
    return db

@app.get("/languages/{lang_id}", response_model=Language)
def get_by_id(lang_id: int):
    for lang in db:
        if lang["id"] == lang_id:
            return lang
    raise HTTPException(status_code=404, detail="Language not found")

@app.post("/languages", response_model=Language)
def add_lang(lang: Language):
    if any(l["id"] == lang.id for l in db):
        raise HTTPException(status_code=400, detail="ID already exists")
    db.append(lang.dict())
    save_data(db)
    return lang

@app.put("/languages/{lang_id}", response_model=Language)
def update_full(lang_id: int, new_lang: Language):
    for i, l in enumerate(db):
        if l["id"] == lang_id:
            db[i] = new_lang.dict()
            save_data(db)
            return new_lang
    raise HTTPException(status_code=404, detail="Language not found")

@app.patch("/languages/{lang_id}")
def patch_lang(lang_id: int, patch: dict):
    for i, l in enumerate(db):
        if l["id"] == lang_id:
            db[i].update(patch)
            save_data(db)
            return db[i]
    raise HTTPException(status_code=404, detail="Language not found")

@app.delete("/languages/{lang_id}")
def delete_lang(lang_id: int):
    global db
    new_db = [l for l in db if l["id"] != lang_id]
    if len(new_db) == len(db):
        raise HTTPException(status_code=404, detail="Language not found")
    db = new_db
    save_data(db)
    return {"msg": "Deleted"}
