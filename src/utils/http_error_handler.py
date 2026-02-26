from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class HTTPErrorHandler(BaseHTTPMiddleware):
    def __init__(self,app: FastAPI)-> None:
        super().__init__(app)

    async def dispatch(self, request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            content = f"Se dio un error al tratar de responder {e} del host {request.client.host}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content=content,status_code=status_code)