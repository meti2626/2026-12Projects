from fastapi import FastAPI
import uvicorn

# Create the FastAPI app instance
app = FastAPI()

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World! This is your Python API."}

# Define an endpoint with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Define a POST endpoint to create data
@app.post("/items/")
def create_item(item: dict):
    return {"message": "Item received", "item": item}

if __name__ == "__main__":
    # Run the API using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
