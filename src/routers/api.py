from fastapi import APIRouter
from src.routers import AuthApi, Todo

router = APIRouter()


router.include_router(Todo.router, prefix='/todo', tags=['Todos'])
router.include_router(AuthApi.router, prefix='/auth', tags=['Auth'])