from fuel_price_api.controls import db_setup

if __name__ == "__main__":
    prod_db_name = "fuel_price.db"
    db_setup.setup_database(prod_db_name)