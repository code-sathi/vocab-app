from fastapi import FastAPI
# from mangum import Mangum //Uncomment this to use mangun in aws lambda
from app.routes import routes

app = FastAPI()

# handler = Mangum(app) //Uncomment this

app.include_router(routes.router)
