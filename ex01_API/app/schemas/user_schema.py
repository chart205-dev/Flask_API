# ============================================
# Userスキーマ
# 入力データのバリデーション・出力データのシリアライズ
# marshmallow を使用
# ============================================

from marshmallow import Schema, fields, validate, ValidationError


class UserSchema(Schema):
    """
    Userスキーマクラス
    リクエスト/レスポンスのデータ構造を定義
    バリデーションルールを設定
    """
    
    # ============ フィールド定義 ============
    # id: 読み取り専用（DBが自動生成）
    id = fields.Int(dump_only=True)
    
    # name: 必須、1～100文字
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=100),
        error_messages={
            'required': 'name は必須です',
            'null': 'name は null にできません'
        }
    )
    
    # age: 整数、1～150
    age = fields.Int(
        required=False,
        allow_none=True,
        validate=validate.Range(min=1, max=150),
        error_messages={
            'validator_failed': 'age は 1 ～ 150 の範囲で指定してください'
        }
    )
    
    # created_at: 読み取り専用、日時形式
    created_at = fields.DateTime(dump_only=True)
    
    # updated_at: 読み取り専用、日時形式
    updated_at = fields.DateTime(dump_only=True)


# スキーマインスタンス
user_schema = UserSchema()
users_schema = UserSchema(many=True)  # 複数ユーザー用