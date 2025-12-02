from app.db.create_database import db
from app.models.item_model import Item
from sqlalchemy.exc import SQLAlchemyError


class ItemService:
    @staticmethod
    def create_item(item_name, price=None):
        try:
            new_item = Item(item_name=item_name, price=price)
            db.session.add(new_item)
            db.session.commit()
            return new_item
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f'Item creation error: {str(e)}')

    @staticmethod
    def get_all_items():
        try:
            items = Item.query.order_by(Item.created_at.desc()).all()
            return items
        except SQLAlchemyError as e:
            raise Exception(f"Item retrieval error: {str(e)}")

    @staticmethod
    def get_item_by_id(item_id):
        try:
            item = Item.query.get(item_id)
            return item
        except SQLAlchemyError as e:
            raise Exception(f"Item retrieval error: {str(e)}")

    @staticmethod
    def update_item(item_id, item_name=None, price=None):
        try:
            item = Item.query.get(item_id)
            if item is None:
                return None
            if item_name is not None:
                item.item_name = item_name
            if price is not None:
                item.price = price
            db.session.commit()
            return item
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Item update error: {str(e)}")

    @staticmethod
    def delete_item(item_id):
        try:
            item = Item.query.get(item_id)
            if item is None:
                return False
            db.session.delete(item)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Item deletion error: {str(e)}")
