# ============================================
# データベース初期化モジュール
# SQLAlchemyのセットアップと初期化を管理
# ============================================

from flask_sqlalchemy import SQLAlchemy

# グローバルなSQLAlchemyインスタンスを作成
# これをアプリケーション全体で使用
db = SQLAlchemy()


def init_db(app):
    """
    アプリケーションにデータベースを初期化
    
    Args:
        app: Flaskアプリケーションインスタンス
    """
    # アプリケーションに db を関連付け
    db.init_app(app)
    
    # アプリケーションコンテキストを確立し、テーブルを作成
    with app.app_context():
        # 既存テーブルの確認とテーブル作成
        db.create_all()
        print("✓ データベーステーブルを作成しました")


def drop_all_tables(app):
    """
    全テーブルを削除（開発用・テスト用）
    
    Args:
        app: Flaskアプリケーションインスタンス
    """
    with app.app_context():
        db.drop_all()
        print("✓ 全テーブルを削除しました")