from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.services.item_service import ItemService
from app.schemas.item_schema import item_schema, items_schema

# Blueprint for /items
item_bp = Blueprint('items', __name__, url_prefix='/items')


@item_bp.route('', methods=['POST'])
def create_item():
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({'error': 'Request body is empty'}), 400

        validated_data = item_schema.load(data)
        
        new_item = ItemService.create_item(
            item_name=validated_data['item_name'],
            price=validated_data.get('price')
        )
        
        result = item_schema.dump(new_item)
        
        return jsonify(result), 201
    
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@item_bp.route('', methods=['GET'])
def get_all_items():
    try:
        items = ItemService.get_all_items()
        result = items_schema.dump(items)
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@item_bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    try:
        item = ItemService.get_item_by_id(item_id)
        if item is None:
            return jsonify({'error': 'Item not found'}), 404
        
        result = item_schema.dump(item)
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@item_bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Request body is empty'}), 400
        
        validated_data = item_schema.load(data, partial=True)
        
        updated_item = ItemService.update_item(
            item_id=item_id,
            item_name=validated_data.get('item_name'),
            price=validated_data.get('price')
        )
        
        if updated_item is None:
            return jsonify({'error': 'Item not found'}), 404
        
        result = item_schema.dump(updated_item)
        return jsonify(result), 200
    
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@item_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        success = ItemService.delete_item(item_id)
        if not success:
            return jsonify({'error': 'Item not found'}), 404
        
        return jsonify({'message': 'Item deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
