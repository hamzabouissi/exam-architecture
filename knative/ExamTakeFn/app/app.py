import json
from typing import Any, Optional, Union
import logging

from app.main import lambda_handler
LOG = logging.getLogger(__name__)
LOG.info("API is starting up")

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    
    return {"Hello": "World"}

@app.get("/")
def intercept_event(object_name:Optional[str]):
    if object_name:
        event = {
            "queryStringParameters": {
                "object_name": object_name
            }
        }
    event = {
        "queryStringParameters": {}
    }
    result = lambda_handler(event=event)
    return result
    