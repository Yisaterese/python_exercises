from alternate_list import alternate_list

def test_alternate_list():
	assert alternate_list(["a","b","c"],[1,2,3]) == ["a",1,"b",2,"c",3]