from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import dc_connector


app = FastAPI(
    title='Domain UI API',
    description='Domain UI API.',
    version='0.1.0',
    prefix='/api/v1/ldap3'
)

app.include_router(dc_connector.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'DELETE'],
    allow_headers=['*'],
)