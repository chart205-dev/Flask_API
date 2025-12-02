# プロジェクト名

XXXXX

## 📘 プロジェクト概要（PJ概要）
このプロジェクトは、XXXXデータを取得するためのアプリケーションです。

## ディレクトリ構成
```
app/
├── __init__.py # create_app (アプリファクトリ) — __init__.py
├── config.py # 設定（development 設定が含まれる） — config.py
├── db/
│ ├── __init__.py
│ └── create_database.py # SQLAlchemy インスタンスと init_db / drop_all — create_database.py
├── models/
│ ├── __init__.py
│ ├── item_model.py # Item モデル定義 — Item
│ └── purchase_model.py # Purchase モデル定義 — Purchase
├── routes/
│ ├── __init__.py
│ ├── item_routes.py # Blueprint（/items） — item_routes.py
│ └── purchase_routes.py # Blueprint（/purchases） — purchase_routes.py
├── schemas/
│ ├── __init__.py
│ ├── item_schema.py # Marshmallow スキーマ — item_schema.py
│ └── purchase_schema.py # Marshmallow スキーマ — purchase_schema.py
└── services/
├── __init__.py
├── item_service.py # ビジネスロジック（DB 操作） — item_service.py
└── purchase_service.py # ビジネスロジック（DB 操作） — purchase_service.py

run.py # 開発用起動スクリプト — run.py
tests/ # テストコード — test_user_api.py
README.md # 本ファイル
requirements.txt # 依存パッケージ
```
## 🗄️ テーブル概要
### テーブル名：items
| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | int | アイテムID（PK） |
| item_name | varchar | アイテム名 |
| price | int | 金額 |
| created_at | datetime | 作成日時 |
| updated_at | datetime | 更新日時 |

### テーブル名：purchases
| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | int | 購入ID（PK） |
| item_id | int | 対応するアイテムの ID（`items.id`） |
| quantity | int | 購入数量 |
| purchased_at | datetime | 購入日時 |
| updated_at | datetime | 更新日時 |