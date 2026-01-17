def setup_module(module):
	print("Setup for module")

def teardown_module(module):
	print("Teardown for module")

def test_example():
		print("Example test")

def test_example2():
	print("Example test 2")

class TestExample():
	def test_hello_world(self):
		print("Hello, World!")

	def test_pytest(self):
		print("Testing with pytest!")