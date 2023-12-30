scores = 0
pass_scores = 0
fail_scores = 0
while scores != -1:
	student_score = int(input("Enter scores or enter -1 to stop: "))
	if (scores < 0 and scores > 100):
		print("Please enter a valid scores")
	if(scores == 45 and scores < 100):
		pass
	if(scores < 45 and scores > 0):
		fail_scores += 1
		pass_score += 1
print(f"The number of students that pass are:{pass_scores} ")	
print("The number of student that fail are:{fail_scores} ")
