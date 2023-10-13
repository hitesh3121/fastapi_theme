import logging
from fastapi import Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.common.error_handler import successResponseSend
from src.controller.Todo import todos_crud
from src.database.database import get_db

class CreateTodoBody(BaseModel):
    task: str
    description: str


router = APIRouter()
logger = logging.getLogger("my_logs")

@router.get("/getTodos")
def read_items(db: Session = Depends(get_db)):
    todos = todos_crud.get_todos(db)
    return successResponseSend(todos)

@router.post("/insertTodo")
def create_todos(todo_value: CreateTodoBody, db:Session = Depends(get_db)):
    inserted =todos_crud.insert_todo(todo_value, db)
    return successResponseSend(inserted)

@router.put("/updateTodo/{todo_id}")
def update_todos(todo_id:str,todo_data:dict, db=Depends(get_db)):
    update_todo= todos_crud.update_todo(todo_id,todo_data,db)
    return update_todo

@router.delete("/deleteTodo/{todo_id}")
def delete_item(todo_id: str, db: Session = Depends(get_db)):
    delete = todos_crud.delete_todo(todo_id, db)
    return successResponseSend(delete)
