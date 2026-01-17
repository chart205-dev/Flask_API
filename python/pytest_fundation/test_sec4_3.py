import pytest

@pytest.fixture(scope="class")
def setup_processing(request):
	print("Setup for processing")
	def teardown_processing():
		print("Teardown for processing")
	request.addfinalizer(teardown_processing)

class TestExample():
	def test_example(self, setup_processing):
		print("Example test")

	def test_example2(self, setup_processing):
		print("Example test 2")