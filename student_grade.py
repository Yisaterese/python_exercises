a_count = 0
b_count = 0
c_count = 0
d_count = 0

for number in range(0,5):
	student_name = str(input("Enter student name\n"))
	student_grade = int(input("Enter studrnt grade\n"))
	if student_grade == 90:
		student
	
	match  student_grade:
		case 90:
			#print(student_name)
			a_count+=1

		case 80:
			#print(student_name)
			b_count+=1
		
		case 70:
			#print(student_name)
			c_count+=1

		case 60:
			#print(student_name)
			d_count+=1

print(f"The number A: {a_count}\nThe number of B: {b_count}\nThe number of C: {c_count}\nThe nmber of D: {d_count}")		
		
	