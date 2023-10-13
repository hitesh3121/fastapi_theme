from src.common.error_handler import successResponseSend
from fastapi import Depends, Response, status, APIRouter
from fastapi.security import HTTPBearer
from src.controller.Auth import VerifyToken


router = APIRouter()

token_auth_scheme = HTTPBearer()

@router.get("/tokenVerify")
def read_items(response: Response ,token: str = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()
    if result.get('status'):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result