class TestExample():
	# 前処理
	def setup_method(self, method):
		print("Setup for function")

	# 後処理
	def teardown_method(self, method):
		print("Teardown for function")
	
	def test_example(self):
		print("Example test")

	def test_example2(self):
		print("Example test 2")