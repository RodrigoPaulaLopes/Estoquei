from fastapi import FastAPI
app = FastAPI()

@app.get("/", tags=["tag"])
async def route_name():
    return {"message": "API de estoque"}