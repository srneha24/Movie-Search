from fastapi import FastAPI, Request, Path
from uuid import UUID

from schemas import Movie, MovieUpdate

app = FastAPI()


@app.post("/movie")
async def insert_movie(request: Request, payload: Movie):
    pass


@app.get("/movie")
async def get_movies(request: Request):
    pass


@app.get("/movie/{movie_id}")
async def get_movie_info(request: Request, movie_id: UUID = Path(...)):
    pass


@app.patch("/movie/{movie_id}")
async def update_movie_info(request: Request, payload: MovieUpdate, movie_id: UUID = Path(...)):
    pass


@app.delete("/movie/{movie_id}")
async def delete_movie(request: Request, movie_id: UUID = Path(...)):
    pass


@app.get("/search")
async def search_movie(request: Request, search: str):
    pass
