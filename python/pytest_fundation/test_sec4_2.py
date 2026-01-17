import pytest

@pytest.fixture()
def setup_processing(request):
	print("Setup for processing")
	def teardown_processing():
		print("Teardown for processing")
	request.addfinalizer(teardown_processing)

class TestExample():
	def test_hello(self, setup_processing):
		print("Hello")

	def test_goodmorning(self):
		print("Good Morning")

	def test_goodafternoon(self, setup_processing):
		print("Good Afternoon")