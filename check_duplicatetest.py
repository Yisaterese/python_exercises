from check_duplicate import check_duplicate


def test_checkduplicate():
	assert check_duplicate(["banana","mango","banana","gwava","apple","apple","apple"]) == ["banana"]