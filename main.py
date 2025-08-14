from fastapi import FastAPI

app = FastAPI(title="Mi API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API"}

@app.get("/hello")
def hello():
    return {"message": "Hola, mundo"}

@app.get("/status")
def status():
    return {"message": "Todo funciona correctamente"}
