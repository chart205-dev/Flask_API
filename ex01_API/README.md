# ============================================
# 0. ヘルスチェック
# ============================================
curl -X GET http://localhost:5000/health


# ============================================
# 1. CREATE（ユーザー作成）
# ============================================

# ユーザー 1 を作成
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d "{\"name\":\"Taro Yamada\",\"age\":30}"

# ユーザー 2 を作成
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d "{\"name\":\"Hanako Suzuki\",\"age\":28}"

# ユーザー 3 を作成（年齢なし）
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d "{\"name\":\"Jiro Sato\"}"

# バリデーションエラー例（nameなし）
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d "{\"age\":25}"


# ============================================
# 2. READ（全件取得）
# ============================================
curl -X GET http://localhost:5000/users


# ============================================
# 3. READ（1件取得）
# ============================================

# ID=1 のユーザーを取得
curl -X GET http://localhost:5000/users/1

# ID=2 のユーザーを取得
curl -X GET http://localhost:5000/users/2

# 存在しないID（ID=999）を取得
curl -X GET http://localhost:5000/users/999


# ============================================
# 4. UPDATE（更新）
# ============================================

# ID=1 のユーザーの name と age を更新
curl -X PUT http://localhost:5000/users/1 -H "Content-Type: application/json" -d "{\"name\":\"Taro Yamada (Updated)\",\"age\":31}"

# ID=2 のユーザーの name のみ更新（部分更新）
curl -X PUT http://localhost:5000/users/2 -H "Content-Type: application/json" -d "{\"name\":\"Hanako Suzuki (Updated)\"}"

# ID=3 のユーザーの age のみ更新
curl -X PUT http://localhost:5000/users/3 -H "Content-Type: application/json" -d "{\"age\":25}"

# 存在しないユーザーを更新
curl -X PUT http://localhost:5000/users/999 -H "Content-Type: application/json" -d "{\"name\":\"Nonexistent User\"}"


# ============================================
# 5. DELETE（削除）
# ============================================

# ID=1 のユーザーを削除
curl -X DELETE http://localhost:5000/users/1

# ID=2 のユーザーを削除
curl -X DELETE http://localhost:5000/users/2

# 存在しないユーザーを削除
curl -X DELETE http://localhost:5000/users/999

# 削除後に全件取得して確認
curl -X GET http://localhost:5000/users
