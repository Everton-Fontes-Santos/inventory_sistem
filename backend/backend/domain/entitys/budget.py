from __future__ import annotations

from .base_entity import BaseEntity

class Budget(BaseEntity):
    """A Budget Entity."""
    title:str = ""
    description:str = ""
    client:str = ""
    
    @staticmethod
    def create(title:str, description:str, client:str)->Budget:
        return Budget(title=title, description=description, client=client)
    