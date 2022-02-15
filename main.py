from turtle import title
from fastapi import FastAPI

app = FastAPI(title= 'Challenge 2',
              description = 'Reto para Data Engineer Jr.',
              version = '1.0.1')

@app.get('/')
async def index():
    return 'Hola mundo, reto challenger'

@app.get('/getclients/ID')
async def about():
    return 'estamos en el abour de getclientes id'