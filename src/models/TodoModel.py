from sqlalchemy import Column, String, DateTime
from src.database.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func

class TodoEntity(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4,
                primary_key=True, unique=True, nullable=False)
    task = Column(String, index=True)
    description = Column(String)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())