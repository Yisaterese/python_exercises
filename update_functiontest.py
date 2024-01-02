from update_function import update_function

def test_update_function():
	assert update_function({1,3,45,34},[10,4,5,2]) == {1,3,45,34,10,4,5,2}