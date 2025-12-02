# ============================================
# Flaskアプリケーション工場
# create_app パターンを採用
# ============================================

from flask import Flask
from app.config import config
from app.db.database import init_db
from app.routes.user_routes import user_bp


def create_app(config_name='development'):
    """
    Flaskアプリケーションを生成する工場関数
    
    Args:
        config_name (str): 設定名（'development', 'testing', 'production'）
    
    Returns:
        Flask: Flaskアプリケーションインスタンス
    
    例：
        app = create_app('development')
        app.run()
    """
    
    # ============ アプリケーション初期化 ============
    # Flaskインスタンスを作成
    app = Flask(__name__)
    
    # ============ 設定を適用 ============
    # 指定された設定をロード
    app.config.from_object(config[config_name])
    
    # ============ データベース初期化 ============
    # SQLAlchemyを初期化（テーブル作成）
    init_db(app)
    
    # ============ Blueprintを登録 ============
    # ユーザー関連のルートを登録（プレフィックス: /users）
    app.register_blueprint(user_bp)
    
    # ============ ヘルスチェックエンドポイント ============
    @app.route('/health', methods=['GET'])
    def health_check():
        """APIが正常に動作しているかを確認"""
        return {'status': 'ok'}, 200
    
    return app