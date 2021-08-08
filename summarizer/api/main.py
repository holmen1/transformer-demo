import uvicorn
from typing import List, Optional
from fastapi import Depends, FastAPI
from transformer import Transformer, get_transformer

import numpy as np


app = FastAPI()
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    # to be matrix
    A: List[List[float]] = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(item: Item):
    A = np.array(item.A)
    U, S, Vh = np.linalg.svd(A)
    return {"U": U.tolist(),"S": S.tolist(),"Vh": Vh.tolist()}



class SummaryRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str


@app.post("/summarize/", response_model=SummaryResponse)
def create_summary(request: SummaryRequest, transformer: Transformer = Depends(get_transformer)):
    summary = transformer.summarize(request.text)
    return SummaryResponse(summary=summary)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)