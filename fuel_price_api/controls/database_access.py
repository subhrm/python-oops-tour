import sqlite3
from unittest import result
from fuel_price_api.data_models.fuel_details import FuelDetails
from typing import List

DB_NAME = "fuel_prices.db"


def add_record(record: FuelDetails) -> None:
    # Connect to database
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    # Insert a row of data
    cur.execute("insert into fuel_details values (?, ?, ?)", (record.location, record.fuel_type, record.price_per_liter))

    # Save (commit) the changes
    con.commit()
    # close connection
    con.close()


def find_by_location(location: str, fuel_type: str) -> FuelDetails:
    # Connect to database
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM fuel_details WHERE location=? AND fuel_type=?", (location, fuel_type))

    # Check result
    results = res.fetchall()
    print(f"Number of recs: {len(results)}")
    if len(results) == 0:
        raise Exception(f"No records fond for the location: {location} and fuel_type: {fuel_type}")

    # close connection
    con.close()
    r = results[0]
    # print(r)
    return FuelDetails(location=r[0], fuel_type=r[1], price_per_liter=r[2])


def list_all() -> List[FuelDetails]:
    # Connect to database
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cursor_res = cur.execute("SELECT * FROM fuel_details")

    # Check result
    results = []
    for r in cursor_res:
        obj = FuelDetails(location=r[0], fuel_type=r[1], price_per_liter=r[2])
        results.append(obj)
    
    # close connection
    con.close()
    return results




def delete_record():
    # Connect to database
    con = sqlite3.connect(DB_NAME)

    # Save (commit) the changes
    con.commit()
    # close connection
    con.close()


def update_record():
    # Connect to database
    con = sqlite3.connect(DB_NAME)

    # Save (commit) the changes
    con.commit()
    # close connection
    con.close()
