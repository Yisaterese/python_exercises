from set_duplicate import my_duplicate

def test_myduplicate():
	assert my_duplicate({True,1,False,0,"banana","add"}) == {True,False,"banana","add"}