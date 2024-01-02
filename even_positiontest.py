from even_position import even_position
from odd_position import odd_position

def test_even_position():
	assert even_position([1,2,3,4,5,6]) == [2,4,6]
	assert odd_position([1,2,3,4,5,6,7]) == [1,3,5]