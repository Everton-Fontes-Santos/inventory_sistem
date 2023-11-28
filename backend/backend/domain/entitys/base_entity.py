from pydantic import BaseModel, Field
from uuid import uuid4

class BaseEntity(BaseModel):
    id:str = Field(str(uuid4()))
    ...