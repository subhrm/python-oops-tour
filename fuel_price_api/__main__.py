from enum import auto
import uvicorn 

from fuel_price_api.routes import app


if __name__ == "__main__":
    # Start the webserver
    uvicorn.run(app, port=8080)
