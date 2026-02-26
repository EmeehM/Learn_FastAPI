from typing import List

from fastapi import Body, Path, Query, APIRouter
from fastapi.responses import HTMLResponse

from src.models.models import Movie


movies : List[Movie] = []
movie_router = APIRouter()

#Query Parameter
#example: /movies/?category=123
@movie_router.get('/mov_cat/',tags=['Movies'])
def get_movie_by_category(category:str = Query(min_length=5)): #Similar to the Path and Body, Query just validation
    return category


@movie_router.post('/',tags=['Movies'])
def create_movie(movie : Movie):
    movies.append(movie.model_dump())
    return HTMLResponse(f'<h1>Movie {moviex} added succesfully!<h1>')


@movie_router.put('/edit/', tags=['Movies'])
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
    
#Parameters
@movie_router.get('/{movie_id}', tags=['Movies'])
def get_movie_by_id(movie_id:int = Path(gt=0)): #The Path func allows us to validate the parameters from the URL
    for movie in movies:
        if movie['id'] == id:    
            return HTMLResponse(f'<h1>Your movie is movie number {movie_id},{movie}<h1>')
    return {}

@movie_router.delete('/delete/', tags=['Movies'])
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