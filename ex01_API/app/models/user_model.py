# ============================================
# Userモデル
# データベースのusersテーブルとマッピング
# ORM層：データベーススキーマを定義
# ============================================

from app.db.database import db
from datetime import datetime


class User(db.Model):
    """
    Userモデルクラス
    PostgreSQL の users テーブルに対応
    """
    # テーブル名を指定
    __tablename__ = 'users'
    
    # ============ カラム定義 ============
    # id: 主キー（自動採番）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # name: ユーザー名（必須、最大100文字）
    name = db.Column(db.String(100), nullable=False)
    
    # age: 年齢（オプション）
    age = db.Column(db.Integer, nullable=True)
    
    # created_at: 作成日時（自動記録）
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # updated_at: 更新日時（自動更新）
    updated_at = db.Column(db.DateTime, nullable=False, 
                          default=datetime.utcnow, 
                          onupdate=datetime.utcnow)
    
    # ============ メソッド ============
    def __repr__(self):
        """オブジェクトの文字列表現（デバッグ用）"""
        return f"<User id={self.id}, name={self.name}, age={self.age}>"
    
    def to_dict(self):
        """
        オブジェクトを辞書に変換
        JSON化する際に使用
        """
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }