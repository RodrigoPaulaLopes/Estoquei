from pydantic import BaseModel, field_validator
import re

class Category(BaseModel):
    name: str
    slug: str
    
    @field_validator('slug')
    def validator_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
             raise ValueError('Invalid Slug')
        return value