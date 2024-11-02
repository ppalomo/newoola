from fastapi import FastAPI
from .content.routers import content_router

app = FastAPI(title="Content Store")


# @app.get("/")
# async def root():
#     return {"service": "content store"}

# Adding routers
app.include_router(content_router)
