from pydantic import BaseModel
# from datetime import datetime

class FuelDetails(BaseModel):
    location:str = "location"
    fuel_type:str = "Petrol"
    price_per_liter:float = 0.0
    # effective_date:datetime = datetime.now()
