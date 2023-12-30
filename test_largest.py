from largest import largest1, product, largest2, largest3


def test_largest():
	assert largest1(2,3,4) == 4
	assert product(2, 4) == 8
	assert largest2(800,12,90,) == 800
	assert largest3(45,89,10) == 89