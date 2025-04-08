from pydantic import BaseModel

class MealRequest(BaseModel):
    diet: str  
    cuisine: str  
    calories: int 
