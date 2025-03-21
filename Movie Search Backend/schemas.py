from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Movie(BaseModel):
    title: str
    poster: Optional[str] = None
    release_date: Optional[date] = None
    director: Optional[str] = None
    synopsis: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)


class MovieUpdate(Movie):
    title: Optional[str] = None
