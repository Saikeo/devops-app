from fastapi import FastAPI, HTTPException
import os

app = FastAPI(title="DevOps Sample Microservice", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "online", "message": "DevOps Microservice is running!"}

@app.get("/health")
def health_check():
    # Basic health check endpoint
    return {"status": "healthy", "environment": os.getenv("ENVIRONMENT", "development")}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be non-negative")
    return {"item_id": item_id, "name": f"Sample Item {item_id}"}
