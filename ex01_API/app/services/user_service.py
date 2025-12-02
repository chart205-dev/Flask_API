# ============================================
# Userサービス層
# ビジネスロジックを担当
# models や db と routes の中間層
# ============================================

from app.db.database import db
from app.models.user_model import User
from sqlalchemy.exc import SQLAlchemyError


class UserService:
    """
    Userサービスクラス
    CRUD操作のビジネスロジックを集約
    """
    
    @staticmethod
    def create_user(name, age=None):
        """
        ユーザーを作成
        
        Args:
            name (str): ユーザー名
            age (int, optional): 年齢
        
        Returns:
            User: 作成されたユーザーオブジェクト
        
        Raises:
            Exception: DB操作エラー
        """
        try:
            # 新しいUserオブジェクトを作成
            new_user = User(name=name, age=age)
            
            # セッションに追加
            db.session.add(new_user)
            
            # コミット（DB保存）
            db.session.commit()
            
            return new_user
        
        except SQLAlchemyError as e:
            # エラーが発生した場合、ロールバック
            db.session.rollback()
            raise Exception(f"ユーザー作成エラー: {str(e)}")
    
    
    @staticmethod
    def get_all_users():
        """
        全ユーザーを取得
        
        Returns:
            list: Userオブジェクトのリスト
        """
        try:
            # 作成日時の昇順でソート
            users = User.query.order_by(User.created_at.desc()).all()
            return users
        
        except SQLAlchemyError as e:
            raise Exception(f"ユーザー取得エラー: {str(e)}")
    
    
    @staticmethod
    def get_user_by_id(user_id):
        """
        IDからユーザーを1件取得
        
        Args:
            user_id (int): ユーザーID
        
        Returns:
            User: ユーザーオブジェクト、存在しない場合はNone
        """
        try:
            user = User.query.get(user_id)
            return user
        
        except SQLAlchemyError as e:
            raise Exception(f"ユーザー取得エラー: {str(e)}")
    
    
    @staticmethod
    def update_user(user_id, name=None, age=None):
        """
        ユーザー情報を更新
        
        Args:
            user_id (int): ユーザーID
            name (str, optional): 新しいユーザー名
            age (int, optional): 新しい年齢
        
        Returns:
            User: 更新されたユーザーオブジェクト、存在しない場合はNone
        
        Raises:
            Exception: DB操作エラー
        """
        try:
            # ユーザーを取得
            user = User.query.get(user_id)
            
            if user is None:
                return None
            
            # 指定されたフィールドを更新
            if name is not None:
                user.name = name
            
            if age is not None:
                user.age = age
            
            # コミット
            db.session.commit()
            
            return user
        
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"ユーザー更新エラー: {str(e)}")
    
    
    @staticmethod
    def delete_user(user_id):
        """
        ユーザーを削除
        
        Args:
            user_id (int): ユーザーID
        
        Returns:
            bool: 削除成功時True、ユーザー不在時False
        
        Raises:
            Exception: DB操作エラー
        """
        try:
            user = User.query.get(user_id)
            
            if user is None:
                return False
            
            # セッションから削除
            db.session.delete(user)
            
            # コミット
            db.session.commit()
            
            return True
        
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"ユーザー削除エラー: {str(e)}")