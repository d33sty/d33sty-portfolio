from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    model_config = ConfigDict(
        str_min_length=1, strict=True
    )  # Pydantic v2: строгий режим


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
