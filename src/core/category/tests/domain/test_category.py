import pytest
import uuid
from src.core.category.domain.category import Category


class TestCategory:
    def test_name_is_require(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name cannot be longer than 255 characters."):
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

    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty."):
            Category(name="")


class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        category = Category(name="Filme", description="Filmes em geral")

        category.update_category(name="Série", description="Séries em geral")

        assert category.name == "Série"
        assert category.description == "Séries em geral"

    def test_update_category_with_invalid_name_raises_exception(self):
        category = Category(name="Filme", description="Filmes em geral")

        with pytest.raises(ValueError, match="name cannot be longer than 255 characters."):
            category.update_category(name="a" * 256, description="Séries em geral")

    def test_cannot_update_category_with_empty_name(self):
        category = Category(name="Filme", description="Filmes em geral")
        with pytest.raises(ValueError, match="name cannot be empty."):
            category.update_category(name="", description="")



class TestActivate:
    def test_activate_inactive_category(self):
        category = Category(
            name="Filme", 
            description="Filmes em geral",
            is_active=False)

        category.activate()
        assert category.is_active is True

    def test_activate_active_caetgory(self):
        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )

        category.activate()
        assert category.is_active is True


class TestDeactivate:
    def test_deactivate_active_category(self):
        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )

        category.deactivate()
        assert category.is_active is False

    def test_deactivate_inactive_category(self):
        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=False
        )

        category.deactivate()
        assert category.is_active is False


class TestEquality:
    def test_when_categories_have_same_id_they_are_equals(self):
        common_id = uuid.uuid4()
        category_1 = Category(name="Filme", id=common_id)
        category_2 = Category(name="Filme", id=common_id)

        assert category_1 == category_2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id = uuid.uuid4()
        category = Category(name="Filme", id=common_id)
        
        dummy = Dummy()
        dummy.id = common_id

        assert category != dummy