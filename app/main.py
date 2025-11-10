from fastapi import FastAPI
app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}
