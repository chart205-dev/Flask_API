from app.db.create_database import db
from app.models.item_model import Item
from sqlalchemy.exc import SQLAlchemyError


class ItemService:
	@staticmethod
	def create_item(name, price=None):
		try:
			new_item = Item(name = name, price = price)
			db.session.add(new_item)
			db.session.commit()
			return new_item
		except SQLAlchemyError as e:
			db.session.rollback()
			raise Exception(f'Product creation error : {str(e)}')