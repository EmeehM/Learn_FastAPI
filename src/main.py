from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse  #There are a lot of responses like plaintext, redirect, Files (Where you can download certain files)
#BaseModel= Model creation, Field= Data validation
from src.routes.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler


app = FastAPI()
app.title = "First API"
app.version = "0.1.0"
app.include_router(router=movie_router, prefix='/movies')
app.add_middleware(HTTPErrorHandler)

@app.get('/', tags=['Home Page'])
def home():
    return HTMLResponse('<h1>Nesfli<h1>')


        



