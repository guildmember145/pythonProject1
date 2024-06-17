from pydantic import BaseModel,Field
from typing import Optional





class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    year: int = Field(le=2022)
    category:str = Field(min_length=5, max_length=15)


    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "year": 2000,
                "category" : "Fantasy"
            }
        }    

    
movies= [{
        "id": 1,
        "title": "Señor de los Anillos:La Comunidad del Anillo",
        "year": 2001,
        "category":"fantasy"
},
{
        "id": 2,
        "title": "Señor de los Anillos:Las dos torres",
        "year": 2002,
        "category":"fantasy"
},
{
        "id": 3,
        "title": "Señor de los Anillos:El retorno del Rey",
        "year": 2003,
        "category":"fantasy"
}



]