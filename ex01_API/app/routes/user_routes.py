# ============================================
# Userルート
# HTTP リクエスト・レスポンスを担当
# Blueprintを使用
# ============================================

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.services.user_service import UserService
from app.schemas.user_schema import user_schema, users_schema

# Blueprintを作成（プレフィックス: /users）
user_bp = Blueprint('users', __name__, url_prefix='/users')


# ============================================
# CREATE（POST）
# ============================================
@user_bp.route('', methods=['POST'])
def create_user():
    """
    ユーザーを作成
    
    Request Body:
        {
            "name": "山田太郎",
            "age": 30
        }
    
    Response:
        201: 作成成功
        400: バリデーションエラー
    """
    try:
        # リクエストボディを JSON で取得
        data = request.get_json()
        
        if data is None:
            return jsonify({'error': 'リクエストボディが空です'}), 400
        
        # スキーマでバリデーション
        validated_data = user_schema.load(data)
        
        # ビジネスロジック層で作成
        new_user = UserService.create_user(
            name=validated_data['name'],
            age=validated_data.get('age')
        )
        
        # スキーマでシリアライズ
        result = user_schema.dump(new_user)
        
        return jsonify(result), 201
    
    except ValidationError as e:
        # バリデーションエラー
        return jsonify({'error': e.messages}), 400
    
    except Exception as e:
        # 予期しないエラー
        return jsonify({'error': str(e)}), 500


# ============================================
# READ（GET 全件）
# ============================================
@user_bp.route('', methods=['GET'])
def get_all_users():
    """
    全ユーザーを取得
    
    Response:
        200: ユーザーリスト
    """
    try:
        users = UserService.get_all_users()
        
        # スキーマでシリアライズ（many=True）
        result = users_schema.dump(users)
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# READ（GET 1件）
# ============================================
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    指定IDのユーザーを1件取得
    
    Args:
        user_id (int): ユーザーID
    
    Response:
        200: ユーザー情報
        404: ユーザーが見つからない
    """
    try:
        user = UserService.get_user_by_id(user_id)
        
        if user is None:
            return jsonify({'error': 'ユーザーが見つかりません'}), 404
        
        result = user_schema.dump(user)
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# UPDATE（PUT）
# ============================================
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    ユーザー情報を更新
    
    Request Body:
        {
            "name": "新しい名前",
            "age": 35
        }
    
    Response:
        200: 更新成功
        404: ユーザーが見つからない
        400: バリデーションエラー
    """
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({'error': 'リクエストボディが空です'}), 400
        
        # 部分更新のため、スキーマで partial=True を指定
        validated_data = user_schema.load(data, partial=True)
        
        # ビジネスロジック層で更新
        updated_user = UserService.update_user(
            user_id=user_id,
            name=validated_data.get('name'),
            age=validated_data.get('age')
        )
        
        if updated_user is None:
            return jsonify({'error': 'ユーザーが見つかりません'}), 404
        
        result = user_schema.dump(updated_user)
        
        return jsonify(result), 200
    
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# DELETE
# ============================================
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    ユーザーを削除
    
    Args:
        user_id (int): ユーザーID
    
    Response:
        200: 削除成功
        404: ユーザーが見つからない
    """
    try:
        success = UserService.delete_user(user_id)
        
        if not success:
            return jsonify({'error': 'ユーザーが見つかりません'}), 404
        
        return jsonify({'message': 'ユーザーを削除しました'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500