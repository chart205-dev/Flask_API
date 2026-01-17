import pytest

@pytest.fixture()
def setup_processing(request):
	print("Setup for processing")
	def teardown_processing():
		print("Teardown for processing")
	request.addfinalizer(teardown_processing)


def test_hello(setup_processing):
	print("Hello Test")

def test_goodmorning():
	print("Good Morning Test")

def test_goodafternoon(setup_processing):
	print("Good Afternoon Test")	

