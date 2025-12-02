from app.db.create_database import db
from datetime import datetime

class Purchase(db.Model):
	__tablename__ = 'purchases'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
	quantity = db.Column(db.Integer, nullable=False)
	purchased_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

	def to_dict(self):
		return {
			'id' : self.id,
			'item_id' : self.item_id,
			'quantity' : self.quantity,
			'purchased_at': self.purchased_at.isoformat() if self.purchased_at else None,
			'updated_at': self.updated_at.isoformat() if self.updated_at else None
		}

