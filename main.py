from fastapi import FastAPI

app = FastAPI()

@app.get("/favicon.ico")
async def favico():
    return None

@app.get("/")
async def root():
    return {"message": "Hello World"}
