from app.schemas.category import Category
import pytest

def category_schema():
    category = Category(name='Roupas', slug='roupas')
    
    print(category.model_dump())
    assert category.model_dump() == {'name': 'Roupas', 'slug': 'roupas'}
    
    
