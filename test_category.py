import pytest
import uuid
from category import Category


class TestCategory:
    def test_name_is_require(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name must have less than 256 characters."):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        assert isinstance(category.id, uuid.UUID)

    def test_create_category_with_default_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.description == ""
        assert category.is_active is True

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Filme")
        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        cat_id = uuid.uuid4()
        category = Category(
            id=cat_id,
            name="Filme", 
            description="Filmes em geral", 
            is_active=False
        )
        assert category.id == cat_id
        assert category.name == "Filme"
        assert category.description == "Filmes em geral"
        assert category.is_active == False

    def test_category_str_return(self):
        cat_id = uuid.uuid4()
        category = Category(
            id=cat_id,
            name="Filme", 
            description="Filmes em geral"
        )
        expected_str = f'{category.name} - {category.description} ({category.is_active})'
        assert str(category) == expected_str

    def test_category_repr_return(self):
        cat_id = uuid.uuid4()
        category = Category(
            id=cat_id,
            name="Filme",
            description="Filmes em geral"
        )
        expected_repr = f"<Category {category.name} ({category.id})>"
        assert repr(category) == expected_repr
