#Models with Pydantic = Basically a class to reuse all along the code
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Movie(BaseModel):
    id : int | None = None #Optional
    title : Optional[str] = Field(max_length=20, frozen = True) # Field() for validation using min_length (str), max_length (str), pattern(str, for regex),  
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
    #VALIDATIONS: nowadays we use decorators like model_validator and field_validator instead of just validator
    @field_validator('title')
    def validate_title(cls,value):
        if len(value) < 5:
            raise ValueError("Title field is shorter than 5 char")
        if len(value) > 20:
            raise ValueError("Title field is longer than 20 char")