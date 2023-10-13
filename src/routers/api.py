from fastapi import APIRouter
from src.routers import AuthApi, Todo

router = APIRouter()

@router.get("/")
async def root():
    print("Hy this is calling main.py of project-FastApi")
    return "Here is respnose of main.py file"

router.include_router(Todo.router, prefix='/todo', tags=['Todos'])
router.include_router(AuthApi.router, prefix='/auth', tags=['Auth'])