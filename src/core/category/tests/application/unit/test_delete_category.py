from unittest.mock import create_autospec
import uuid

import pytest
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest

from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.domain.category import Category


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        category = Category(
            name="Filme",
            description="Categoria de filmes"
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = DeleteCategory(mock_repository)
        use_case.execute(DeleteCategoryRequest(id=category.id))

        mock_repository.delete.assert_called_once_with(category.id)


    def test_when_category_not_found_then_raise_expection(self):

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = None

        id_category = uuid.uuid4()
        err_msg = f"Category with {id_category} not found."

        use_case = DeleteCategory(mock_repository)

        with pytest.raises(CategoryNotFound, match=err_msg):
            use_case.execute(DeleteCategoryRequest(id=id_category))

        mock_repository.delete.assert_not_called()
