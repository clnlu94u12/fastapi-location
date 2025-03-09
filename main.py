from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    text: str
    prefecture: str

@app.post("/convert_location")
def convert_location(data: RequestData):
    return {"converted_text": f"変更後: {data.text}", "new_prefecture": "ランダムな都道府県"}


