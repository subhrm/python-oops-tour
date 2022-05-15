from typing import List
from fastapi import APIRouter, HTTPException

from fuel_price_api.data_models.fuel_details import FuelDetails
from fuel_price_api.controls.database_access import add_record, find_by_location, list_all

router = APIRouter(prefix="/fuel_prices")

@router.post("/add")
async def add_fuel_record(record:FuelDetails) -> FuelDetails:
    try:
        add_record(record)
        return record
    except Exception as e:
        return HTTPException(500, "Server Could not add the record")

    

@router.get("/getall")
async def find_fuel_record() -> List[FuelDetails]:
    try:
        return list_all()
    except Exception as e:
        return HTTPException(500, "Server Could not find the record")



@router.get("/search/{location}/{fuel_type}")
async def find_fuel_record(location:str, fuel_type:str) -> FuelDetails:
    try:
        return find_by_location(location, fuel_type)
    except Exception as e:
        return HTTPException(500, "Server Could not find the record")


