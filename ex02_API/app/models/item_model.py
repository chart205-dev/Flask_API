from app.db.create_database import db
from datetime import datetime

class Item(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	item_name = db.Column(db.String(64), nullable=False)
	price = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

	def to_dict(self):
		return {
			'id' : self.id,
			'item_name' : self.item_name,
			'price' : self.price,
			'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
		}

