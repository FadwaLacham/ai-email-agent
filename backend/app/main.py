from fastapi import FastAPI

app = FastAPI(
    title="AI Email Agent",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Email Agent is running!"
    }