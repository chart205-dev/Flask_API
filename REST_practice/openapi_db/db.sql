CREATE TABLE qa_history (
	id SERIAL PRIMARY KEY,
	question_text TEXT,
	answer_text TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)