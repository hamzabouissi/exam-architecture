from typing import Any, Union
import logging
from main import handler
LOG = logging.getLogger(__name__)
LOG.info("API is starting up")

from fastapi import FastAPI,Request

app = FastAPI()


@app.get("/health")
def health():
    
    return {"Hello": "World"}

@app.post("/",status_code=200)
async def intercept_event(request:Request):
    event = await request.json()
    print(event)
    LOG.info(event)
    handler(event,{})
    return "good"
    