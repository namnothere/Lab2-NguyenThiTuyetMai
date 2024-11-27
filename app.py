import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/")
async def home():
    return """
    <h2>HOMEPAGE</h2>
"""

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=80)