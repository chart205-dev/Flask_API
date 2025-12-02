from flask import Blueprint


item_bp = Blueprint('items', __name__, url_prefix='/items')

@item_bp.route('')
def get_item_info():
	return []