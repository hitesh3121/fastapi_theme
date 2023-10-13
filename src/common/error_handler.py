from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(exc.detail, status_code=exc.status_code)


def successResponseSend(data, status_code=200):
    response = {"status": "success" if status_code ==
                200 else "error", "data": data}
    return response
