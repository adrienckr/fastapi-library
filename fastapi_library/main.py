from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the book API!"}

@app.get("/books")
def get_books():
    return []

