from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(min_length=2, max_length=10)
    age: int = Field(ge=0, le=19)
    gender: str | None = None

@app.post("/users")
def create_user(user: User):
    return {"name": user.name, "age": user.age, "gender": user.gender}