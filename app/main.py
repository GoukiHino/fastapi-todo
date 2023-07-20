from fastapi import FastAPI

from app.api.v1 import api
from app.core.config import settings

app = FastAPI()
app.include_router(api.router, prefix=settings.API_PREFIX)
