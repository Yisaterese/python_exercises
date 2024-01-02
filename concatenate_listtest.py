from concatenate_list import concatenate_list

def test_concatenate_list():
	assert concatenate_list(["a","b","c"],[1,2,3]) == ["a","b","c",1,2,3]