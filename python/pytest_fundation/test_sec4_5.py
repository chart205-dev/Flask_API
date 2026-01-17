import pytest

@pytest.fixture(autouse = True)
def setup_processing(request):
	print("Setup for processing")
	def teardown_processing():
		print("Teardown for processing")
	request.addfinalizer(teardown_processing)


class TestExample():
	def test_hello(self):
		print("Hello Test")

	def test_goodmorning(self):
		print("Good Morning Test")

	def test_goodafternoon(self):
		print("Good Afternoon Test")	

