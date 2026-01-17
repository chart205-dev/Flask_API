import pytest

@pytest.fixture(scope="module")
def setup_module(request):
	print("Setup for module")
	def teardown_module():
		print("Teardown for module")
	request.addfinalizer(teardown_module)

@pytest.fixture(scope="function")
def setup_function(request):
	print("Setup for function")
	def teardown_function():
		print("Teardown for function")
	request.addfinalizer(teardown_function)

def test_example(setup_module, setup_function):
		print("Example test")

def test_example2(setup_module):
	print("Example test 2")

class TestExample():
	def test_hello_world(self, setup_module):
		print("Hello, World!")

	def test_pytest(self, setup_module):
		print("Testing with pytest!")