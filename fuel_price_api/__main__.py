import uvicorn 

from fuel_price_api.routes import app

# This is exc=ecuted automatically when you run "pythom -m" commands

if __name__ == "__main__":
    # Start the webserver
    uvicorn.run(app, port=8080)
