from fastapi import FastAPI
from app.routers.coffees import router as coffees_router

description = """
Coffees API helps you to choice the best coffee to you!
You can read about coffee body resulting from origin and beverage methods.

I'm sure you mathc the best beverage for you. 

If you are the coffeeholic this app is for you
"""


app = FastAPI(
    title="CoffeesAPP",
    description=description,
    version="0.0.1",
    contact={"name": "Patrycja", "email": "patrycjamzn@gmail.com"},
)

app.include_router(coffees_router)
