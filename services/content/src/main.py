from fastapi import FastAPI
from .sources.routers import sources_router
from .content.routers import content_router

app = FastAPI(title="Content Store")

# Adding routers
app.include_router(sources_router)
app.include_router(content_router)
