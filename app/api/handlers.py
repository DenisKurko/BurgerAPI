from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from db.core import NotFoundError


def exception_handler(app: FastAPI) -> None:
    @app.exception_handler(NotFoundError)
    async def not_found_error_exception_handler(request: Request, exc: NotFoundError):
        return JSONResponse(status_code=404, content={"detail": str(exc)})