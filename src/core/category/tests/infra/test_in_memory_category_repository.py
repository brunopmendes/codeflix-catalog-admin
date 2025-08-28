import pytest

from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

class TestSave:
    def test_can_save_category(self):
        
        repository = InMemoryCategoryRepository()
        category = Category(
            name="Filme",
            description="Categoria para filmes"
        )
        repository.save(category)

        assert len(repository.categories) == 1
        assert repository.categories[0] == category

class TestGetById:
    def test_can_get_category_by_id(self):
        repository = InMemoryCategoryRepository()
        category = Category(
            name="Filme",
            description="Categoria para filmes"
        )
        repository.save(category)

        category_response = repository.get_by_id(category.id)
        assert category_response.name == 'Filme'
        assert category_response.description == 'Categoria para filmes'


class TestDeleteById:
    def test_can_delete_category_by_id(self):
        
        category_filme = Category(
            name="Filme",
            description="Categoria para filmes",
            is_active=True
        )
        category_serie = Category(
            name="Série",
            description="Categoria para séries",
            is_active=True
        )
        repository = InMemoryCategoryRepository(
            categories=[
                category_filme,
                category_serie
            ]
        )
        
        assert len(repository.categories) == 2
        repository.delete(id=category_filme.id)
        assert len(repository.categories) == 1