from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse , JSONResponse #There are a lot of responses like plaintext, redirect, Files (Where you can download certain files)
from pydantic import BaseModel, Field #BaseModel= Model creation, Field= Data validation
from typing import Optional , List

app = FastAPI()
app.title = "First API"
app.version = "0.1.0"

movies : List[Movie] = []

#Models with Pydantic = Basically a class to reuse all along the code
class Movie(BaseModel):
    id : int | None = None #Optional
    title : Optional[int] = Field(max_length=20, frozen = True) # Field() for validation using min_length (str), max_length (str), pattern(str, for regex),  
                                    # gt (greater than, numbers), lt (number), default, title, description, example for defining the whole data field
                                    # alias for using a diferent name in the json than in the python file, exclude to hide data from the json or dict
                                    # frozen to make an object unmodifiable
    overview : str  
    year : int 
    rating : float 
    category : str 

    model_config = {   #Configurations of the model for example to specify the exmaple values, you could also di this in the Field() using default=
        'json_schema_extra' : {
            'example' : {
                'id' : 1,
                'title' : 'Film Name',
                'overview' : 'Short explanation about the movie',
                'year' : 1999 ,
                'rating' : 6.5, 
                'category' : 'Comedy' ,
            }
        }
    }


@app.get('/', tags=['Home Page'])
def home():
    return HTMLResponse('<h1>Nesfli<h1>')

#Parameters
@app.get('/movies/{movie_id}', tags=['Movies'])
def get_movie_by_id(movie_id:int = Path(gt=0)): #The Path func allows us to validate the parameters from the URL
    for movie in movies:
        if movie['id'] == id:    
            return HTMLResponse(f'<h1>Your movie is movie number {movie_id},{movie}<h1>')
    return {}
        
#Query Parameter
#example: /movies/?category=123
@app.get('/movies/',tags=['Movies'])
def get_movie_by_category(category:str = Query(min_length=5)): #Similar to the Path and Body, Query just validation
    return category


@app.post('/movies',tags=['Movies'])
def create_movie(movie : Movie):
    movies.append(movie.model_dump())
    return HTMLResponse(f'<h1>Movie {movie} added succesfully!<h1>')


@app.put('/movies/edit/', tags=['Movies'])
def edit_movie(movie: Movie):
    for item in movies:
        if item.id == id:
            item["id"] = movie.id
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return HTMLResponse(f'<h1>The movie With the id {id} is now the movie {movie}')
    return HTMLResponse(f'<h1>No movie with the id {id} found! <h1>')
    

@app.delete('/movies/delete/', tags=['Movies'])
def delete_movie(id : int = Body(), 
                 title : str = Body() , 
                 overview : str = Body(), 
                 year : int = Body(), 
                 rating : float = Body(), 
                 category : str = Body()):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return HTMLResponse(f'<h1>Movie with id {id} has been eliminated<h1>')
    return HTMLResponse(f'<h1>No movie with id {id} found! <h1>')


