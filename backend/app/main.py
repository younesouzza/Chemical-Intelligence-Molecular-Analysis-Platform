from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.config import settings
from app.api.routes.molecules import router as molecules_router

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "detail": str(exc)},
    )

app.include_router(molecules_router)

@app.get("/")
def root():
    return {"status": "healthy", "project": settings.PROJECT_NAME}