# 様々な関数のテストを例示
def test_calculate():
	result = 5 * 2
	assert result == 10

def test_len():
	text = "pytest"
	assert len(text) == 6

def test_contains():
	items = [1, 2, 3, 4, 5]
	assert 3 in items