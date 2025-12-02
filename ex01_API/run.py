# ============================================
# アプリケーション起動スクリプト
# このファイルを実行してアプリを起動
# ============================================

from app import create_app

if __name__ == '__main__':
    """
    開発環境でのアプリケーション実行
    
    実行コマンド:
        python run.py
    
    出力例:
        * Running on http://127.0.0.1:5000
        * Debug mode: on
    """
    
    # development 設定でアプリを生成
    app = create_app('development')

    
    # 開発サーバーを起動
    # debug=True: コード変更時に自動リロード、詳細なエラー表示
    # host='0.0.0.0': 全インターフェースでリッスン
    # port=5000: ポート番号
    app.run(debug=True, host='127.0.0.1', port=5000)