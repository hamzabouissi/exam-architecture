from typing import Any, Union
import logging
LOG = logging.getLogger(__name__)
LOG.info("API is starting up")

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    
    return {"Hello": "World"}

@app.post("/")
def intercept_event(req:Any):
    LOG.info(req)
    print(req)
    