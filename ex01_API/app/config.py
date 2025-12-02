# ============================================
# 設定ファイル
# アプリケーション全体で使用する設定をここに定義
# .env は使わず、DB接続情報を直接記述
# ============================================

import os
from datetime import timedelta

class Config:
    """
    基本設定クラス
    全環境共通の設定を定義
    """
    # SQLAlchemy の基本設定
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 変更追跡を無効（パフォーマンス向上）
    SQLALCHEMY_ECHO = True  # SQL文をログに出力（デバッグ用）


class DevelopmentConfig(Config):
    """
    開発環境の設定
    PostgreSQL の接続情報を直接記述
    """
    # PostgreSQL接続URI
    # 形式: postgresql://ユーザー名:パスワード@ホスト:ポート/データベース名
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/flask_api_db"
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """テスト環境の設定"""
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/flask_api_test"
    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    """本番環境の設定"""
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@production-host:5432/flask_api_prod"
    DEBUG = False
    TESTING = False


# 実行環境に応じて設定を選択
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}