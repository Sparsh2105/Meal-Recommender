from fastapi import APIRouter
from models import MealRequest
import requests

router = APIRouter()

@router.post("/recommend")
def recommend_meal(meal_request: MealRequest):
    
    API_URL = f"https://api.spoonacular.com/recipes/complexSearch?diet={meal_request.diet}&cuisine={meal_request.cuisine}&maxCalories={meal_request.calories}&apiKey=d7b0f7c5f12548cc8dbab381567c12c8"
    
    response = requests.get(API_URL)
    data = response.json()
    
    return {"recommended_meals": data.get("results", [])}
