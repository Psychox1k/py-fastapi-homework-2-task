import datetime

from pydantic import BaseModel, ConfigDict


class Country(BaseModel):
    id: int
    code: str
    name: str | None

class Actor(BaseModel):
    id: int
    name: str

class Genre(BaseModel):
    id: int
    name: str

class Language(BaseModel):
    id: int
    name: str

class Movie(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    overview: str

    model_config = ConfigDict(from_attributes=True)



class MovieBase(BaseModel):
    name: str
    date: datetime.date
    score: float
    overview: str
    status: str
    budget: float
    revenue: float


class MovieCreateSchema(MovieBase):
    country: str
    actors: list[str]
    genres: list[str]
    languages: list[str]


class MovieUpdateSchema(BaseModel):
    name: str | None = None
    date: datetime.date | None = None
    score: float | None = None
    overview: str | None = None
    status: str | None = None
    budget: float | None = None
    revenue: float | None = None


class MovieDetailSchema(MovieBase):
    id: int

    country: Country
    actors: list[Actor]
    genres: list[Genre]
    languages: list[Language]

    model_config = ConfigDict(from_attributes=True)

class MovieListSchema(BaseModel):
    movies: list[Movie]
    prev_page: str | None
    next_page: str | None
    total_pages: int
    total_items: int