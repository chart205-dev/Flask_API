from marshmallow import Schema, fields, validate, ValidationError

class ItemSchema(Schema):
	id = fields.Int(dump_only=True)
	item_name = fields.Str(
		required = True,
		validate = validate.Length(min=1, max=100),
		error_messages = {
			'required' : 'Name is required',
			'null' : 'name cannot be null'
		}
	)

	price = fields.Int(
		required = True,
		validate = validate.Range(min=0),
		error_messages = {
			'validator_failed' : 'Please set it to 0 yen or more.'
		}
	)

	created_at = fields.DateTime(dump_only=True)
	updated_at = fields.DateTime(dump_only=True)

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
