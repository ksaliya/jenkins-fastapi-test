from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def status():
    return {"status": "success", "message": "API running"}