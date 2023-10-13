from fastapi import APIRouter, HTTPException
from src.models.TodoModel import TodoEntity
from sqlalchemy.orm import Session


router = APIRouter()

class TodoCrud:
    def __init__(self, model):
        self.model = model
        
    def get_todos(self, db=Session):
        todos = db.query(self.model).all()
        return todos
    
    def get_todo(self, todo_id: int, db=Session):
        todo = db.query(self.model).filter(self.model.id == todo_id).first()
        return todo
    
    def insert_todo(self, todo, db=Session):
        db_todo = self.model(task=todo.task, description=todo.description)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    
    def update_todo(self, todo_id:str,todo_data, db=Session):
        db_todo = db.query(self.model).filter(self.model.id == todo_id).first()
        for key, value in todo_data.items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    
    def delete_todo(self, todo_id:str, db=Session):
        db_todo = db.query(self.model).filter(self.model.id == todo_id).first()
        if db_todo:
            db.delete(db_todo)
            db.commit()
            return {"Message": "Todo deleted successfully!!"}
        else:
            raise HTTPException(status_code=404, detail="Todo not found!!")

        
todos_crud = TodoCrud(TodoEntity)