CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

-- データ挿入
INSERT INTO users (name, age) VALUES
('Taro', 20),
('Hanako', 25),
('Jiro', 30);

-- データ確認
SELECT * FROM users;