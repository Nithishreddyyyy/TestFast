from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def DeploymentCheck():
    return "The deployment is successful"