from zeroed import zeroed

def test_zeroed():
	assert zeroed([1,2,3,4,5]) == [0,2,3,4,0]