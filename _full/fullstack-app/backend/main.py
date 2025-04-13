from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
#from app.api import chat  # importa il file che hai appena creato
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Carica il modello GPT-2 e il tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

#app.include_router(chat.router, prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/api/user")
def get_users():
    return {"message": "Hello, this is a simple service!"}

# Pydantic model per il corpo della richiesta
class ChatMessage(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(message: ChatMessage):
    # Tokenizza il messaggio in input
    inputs = tokenizer.encode(message.message, return_tensors="pt")

    # Genera la risposta usando GPT-2
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)

    # Decodifica la risposta generata
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"response": response}
