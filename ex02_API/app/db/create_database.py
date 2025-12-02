import logging
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
_logger = logging.getLogger(__name__)

def init_db(app):
    db.init_app(app)

    with app.app_context():
        # models を import して metadata に登録させる（ここを確実に）
        try:
            from app.models import item_model  # noqa: F401
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