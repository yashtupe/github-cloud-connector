from fastapi import FastAPI
from app.routes import github

app = FastAPI(title="GitHub Cloud Connector")

app.include_router(github.router)

@app.get("/")
def home():
    return {"message": "GitHub Connector is running 🚀"}