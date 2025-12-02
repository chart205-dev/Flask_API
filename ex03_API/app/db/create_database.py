import logging
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
_logger = logging.getLogger(__name__)

def init_db(app):
    db.init_app(app)

    with app.app_context():
        try:
            from app.models import item_model, purchase_model 
        except Exception as e:
            _logger.exception("モデルのインポートに失敗しました: %s", e)
            raise

        try:
            db.create_all()
            _logger.info("✓ データベーステーブルを作成しました")
        except Exception as e:
            _logger.exception("DB テーブル作成に失敗しました: %s", e)
            raise

def drop_all_tables(app):
    """
    全テーブルを削除（開発用・テスト用）
    
    Args:
        app: Flaskアプリケーションインスタンス
    """
    with app.app_context():
        db.drop_all()
        print("✓ 全テーブルを削除しました")