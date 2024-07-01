from sqlalchemy.orm import Session
from sqlalchemy.sql import not_

from ....app import (
    crud,
    models,
    schemas,
)


def test_can_create_item_category(mocker):
    # Mock DB Session
    mock_session = mocker.Mock(spec=Session)

    # Create schema and model
    schema = schemas.ItemCategoryCreate(name="1")
    model = models.ItemCategory(**schema.model_dump())
    model.id = 1

    # Add side effect to the session.refresh method
    def refresh_side_effect(obj):
        for key, value in model.__dict__.items():
            setattr(obj, key, value)

    mock_session.refresh.side_effect = refresh_side_effect

    # Run
    result = crud.create_item_category(db=mock_session, item_category=schema)

    # Assert the expected behavior
    mock_session.add.assert_called_once_with(mocker.ANY)
    args, _ = mock_session.add.call_args
    assert isinstance(args[0], models.ItemCategory)

    mock_session.commit.assert_called_once()

    mock_session.refresh.assert_called_once_with(mocker.ANY)
    args, _ = mock_session.refresh.call_args
    assert isinstance(args[0], models.ItemCategory)

    assert result.to_dict() == model.to_dict()


def test_can_read_item_category(mocker):
    # Mock DB
    mock_session = mocker.Mock(spec=Session)

    # Create Model
    model = models.ItemCategory(id=1, name="1")

    mock_query = mock_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_filter.first.return_value = model
    # Run
    result = crud.read_item_category(db=mock_session, id=1)

    mock_session.query.assert_called_once_with(mocker.ANY)
    args, _ = mock_session.query.call_args
    assert args[0] == models.ItemCategory

    mock_query.filter.assert_called_once_with(mocker.ANY, mocker.ANY)
    args, _ = mock_query.filter.call_args
    assert str(args[1]) == str(not_(models.ItemCategory.is_deleted))

    mock_filter.first.assert_called_once()

    assert result.to_dict() == model.to_dict()


def test_can_create_item_categories(mocker):
    # Mock DB
    mock_db_session = mocker.Mock(spec=Session)

    test_models = []

    offset_value = 0
    limit_value = 10

    for i in range(offset_value + 1, limit_value + 1):
        model = models.ItemCategory(id=i, name=str(i))
        test_models.append(model)

    mock_query = mock_db_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_offset = mock_filter.offset.return_value
    mock_limit = mock_offset.limit.return_value
    mock_limit.all.return_value = test_models[offset_value:limit_value]

    # Run
    result = crud.read_item_categories(
        db=mock_db_session, skip=offset_value, limit=limit_value
    )

    mock_db_session.query.assert_called_once_with(mocker.ANY)
    args, _ = mock_db_session.query.call_args
    assert args[0] == models.ItemCategory

    mock_query.filter.assert_called_once_with(mocker.ANY)
    args, _ = mock_query.filter.call_args
    assert str(args[0]) == str(not_(models.ItemCategory.is_deleted))

    mock_filter.offset.assert_called_once_with(offset_value)

    mock_offset.limit.assert_called_once_with(limit_value)

    assert [x.to_dict() for x in result] == [
        x.to_dict() for x in test_models[offset_value:limit_value]
    ]


def test_can_update_item_category(mocker):
    # Mock DB
    mock_session = mocker.Mock(spec=Session)

    # Create Model and schema
    model = models.ItemCategory(id=1, name="1")
    schema = schemas.ItemCategoryUpdate(name="2")

    # Patch dependencies
    mocker.patch("bellerouze_pos_2.app.crud.read_item_category", return_value=model)

    # Run
    result = crud.update_item_category(db=mock_session, id=1, update_model=schema)

    mock_session.commit.assert_called_once()

    mock_session.refresh.assert_called_once_with(mocker.ANY)
    args, _ = mock_session.refresh.call_args
    assert isinstance(args[0], models.ItemCategory)

    assert model.to_dict() == result.to_dict()


def test_update_item_category_not_found(mocker):
    # Mock DB
    mock_session = mocker.Mock(spec=Session)

    # Create Schema
    schema = schemas.ItemCategoryUpdate(name="2")

    # Patch dependencies
    mocker.patch("bellerouze_pos_2.app.crud.read_item_category", return_value=None)

    # Run
    result = crud.update_item_category(db=mock_session, id=1, update_model=schema)

    mock_session.commit.assert_not_called()
    mock_session.refresh.assert_not_called()

    assert result is None
