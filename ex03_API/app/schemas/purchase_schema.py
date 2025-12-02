from marshmallow import Schema, fields, validate, ValidationError, validates
from app.models.item_model import Item  

class PurchaseSchema(Schema):
    id = fields.Int(dump_only=True)

    item_id = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    @validates('item_id')
    def validate_item_id(self, value):
        # DBに存在するかチェック
        if not Item.query.get(value):
            raise ValidationError(f"Item with id {value} does not exist.")

    quantity = fields.Int(
        required=True,
        validate=validate.Range(min=1),
        error_messages={
            'validator_failed': 'Please set it to 1 or more.'
        }
    )

    purchased_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)
