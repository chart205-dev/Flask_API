import pytest


def test_hello():
	print("Hello Test")

@pytest.mark.skip(reason="write erason")
def test_goodmorning():
	print("Good Morning Test")

def test_goodafternoon():
	print("Good Afternoon Test")