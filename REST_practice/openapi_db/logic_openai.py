from openai import OpenAI
import json
 

with open("key.json", "r", encoding="utf-8") as f:
    api_key = json.load(f)

client = OpenAI(api_key = api_key["SecretKey"])

# ChatGPT APIからのレスポンスを取得する
def answer_by_chatgpt(prompt):
    response = client.chat.completions.create(
		model="gpt-5-nano",
		messages=[
			{"role": "system", "content": "あなたは常に日本語で回答する有用なアシスタントです。"},
			{"role": "user", "content": prompt}
		]
	)
    return response.choices[0].message.content


if __name__ == "__main__":
    print("エラーなし")