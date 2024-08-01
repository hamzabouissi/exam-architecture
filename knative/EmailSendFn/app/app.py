from typing import Any, Union
import logging
from main import main
LOG = logging.getLogger(__name__)
LOG.info("API is starting up")

from fastapi import FastAPI,Request

app = FastAPI()


@app.get("/health")
def health():
    
    return {"Hello": "World"}

@app.post("/")
async def intercept_event(request:Request):
    event = await request.body()
    LOG.info(event)
    return main(event,None)

    