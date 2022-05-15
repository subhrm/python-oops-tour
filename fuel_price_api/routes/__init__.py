from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """ 
    Default root route
    For Testing api is up or not. No actual business function
    """
    return {"Hello": "World"}


from .fuel_route import router 
app.include_router(router)