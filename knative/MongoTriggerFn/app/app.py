from typing import Any, Union
import logging
from main import lambda_handler

LOG = logging.getLogger(__name__)
LOG.info("API is starting up")

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/health")
def health():
    return {"Hello": "World"}


@app.post("/")
async def intercept_event(request: Request):
    event = await request.json()
    return lambda_handler(event, None)
