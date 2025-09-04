import pytest
from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound, InvalidCategoryData

class TestUpdateCategory:
    def test_can_update_category_name_and_description(self):
        category = Category(
            name="Filme",
            description="Categoria para filmes"
        )

        repository = InMemoryCategoryRepository()
        repository.save(category=category)

        use_case = UpdateCategory(repository=repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name="Série",
            description="Categoria para séries"
        )
        use_case.execute(request=request)

        update_category = repository.get_by_id(category.id)
        assert update_category.name == "Série"
        assert update_category.description == "Categoria para séries"


    def test_update_category_with_invalid_data(self):
        category = Category(
            name="Filme",
            description="Categoria para filmes"
        )

        repository = InMemoryCategoryRepository()
        repository.save(category=category)
        
        use_case = UpdateCategory(repository=repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name=12
        )
        with pytest.raises(InvalidCategoryData):
            use_case.execute(request=request)


    def test_update_category_with_none_category(self):
        category = Category(
            name="Filme",
            description="Categoria para filmes"
        )

        repository = InMemoryCategoryRepository()
        repository.save(category=category)
        
        use_case = UpdateCategory(repository=repository)
        request = UpdateCategoryRequest(
            id=123, #id nao existe
            name=12
        )
        with pytest.raises(CategoryNotFound):
            use_case.execute(request=request)
