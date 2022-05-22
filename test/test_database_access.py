import os
import pytest
from fuel_price_api.controls import database_access as da
from fuel_price_api.controls import db_setup
from fuel_price_api.data_models.fuel_details import FuelDetails

print("Setting up database")
da.DB_NAME = "test.db"
if os.path.exists(da.DB_NAME):
    # delete db if exists
    os.remove(da.DB_NAME)
db_setup.setup_database(da.DB_NAME)
print("Database setup done")

def test_add_record_and_find_record():
    record = FuelDetails(location="kalahandi", fuel_type="Petrol", price_per_liter=200)
    da.add_record(record)
    assert True
    price = da.find_by_location("kalahandi", "Petrol")
    assert price.price_per_liter == 200


@pytest.mark.parametrize(
    "location, fuel_type, price_per_liter",
    [
        ("kalahandi", "Petrol", 200),
        ("ରଘୁନାଥପୁର", "Diesel", 100),
        ("ରଘୁନାଥପୁର", "CNG", 75),
        ("ପଟନା", "Petrol", 100),
        ("दिल्ली", "Petrol", 100),
    ],
)
def test_add_record_and_find_record_edge_cases(location, fuel_type, price_per_liter):
  
    # make sure the database is created
    assert os.path.exists(da.DB_NAME)
    record = FuelDetails(location=location, fuel_type=fuel_type, price_per_liter=price_per_liter)
    da.add_record(record)
    assert True
    price = da.find_by_location(location, fuel_type)
    assert price.price_per_liter == price_per_liter


# def test_search_for_non_existing_record():
#     assert da.find_by_location("kalahandi", "Petrol") 
#     assert da.find_by_location("london", "Petrol").price_per_liter == 200
