#Q-4 In your last program where you find the total and percentage of a student's marks of 5 subject,
#  find the grade of the student using conditional statement. Eg. grade 'A' if percentage is greator
#  than or equals to 60, 'B' for  percentage is greator than or equals to 50 and less than 60,  'C'
#  for  percentage is greator than or equals to 40 and less than 50,  'D' for  percentage is greator 
# than or equals to 33 and less than 40, otherwise 'Fail'

#Solution

# Student Result Program with Grade

name = input("Enter student name: ")
student_class = input("Enter class: ")

total = 0

# Taking marks of 5 subjects
for i in range(1, 6):
    marks = int(input(f"Enter marks of subject {i}: "))
    total += marks

# Calculating percentage
percentage = total / 5

# Finding grade
if percentage >= 60:
    grade = "A"

elif percentage >= 50 and percentage < 60:
    grade = "B"

elif percentage >= 40 and percentage < 50:
    grade = "C"

elif percentage >= 33 and percentage < 40:
    grade = "D"

else:
    grade = "Fail"

# Displaying result
print(f"""
----- RESULT -----

Name       : {name}
Class      : {student_class}
Total      : {total}
Percentage : {percentage}%
Grade      : {grade}

""")