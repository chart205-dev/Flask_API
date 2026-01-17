from translator import GoogleTranslator
import pytest

@pytest.fixture(scope="module")
def trans():
	t = GoogleTranslator()
	print("create translator")
	return t

def test_japanese_to_english(trans):
	test_translated = trans.convert("私の名前は佐藤です.", "日本語", "英語")
	assert test_translated == "My name is Sato."

def test_english_to_japanese(trans):
	test_translated = trans.convert("I love programming.", "英語", "日本語")
	assert test_translated == "私はプログラミングが大好きです。"