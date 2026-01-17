class TestExample():
	@classmethod
	def setup_class(cls):
		print("Setup for class")

	@classmethod
	def teardown_class(cls):
		print("Teardown for class")
	
	def test_example(self):
		print("Example test")

	def test_example2(self):
		print("Example test 2")