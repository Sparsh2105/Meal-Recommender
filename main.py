from fastapi import FastAPI
from routes import meal

app = FastAPI()

app.include_router(meal.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Meal Recommender API!"}
