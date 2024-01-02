from extend_and_reverse import extend_and_reverse
from extend_and_reverse import extend_and_reverse2
from extend_and_reverse import extend_and_reverse3



def test_extend_and_reverse():
	assert extend_and_reverse(["a","b","c"],[1,2,3]) == [3,2,1,"c","b","a"]
	assert extend_and_reverse2(["a","b","c"],[1,2,3]) == [3,2,1,"c","b","a"]
	assert extend_and_reverse3(["a","b","c"],[1,2,3]) == [3,2,1,"c","b","a"]