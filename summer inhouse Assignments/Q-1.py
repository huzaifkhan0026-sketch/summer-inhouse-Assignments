#Q-1) Write a python program that takes in a student name, class. It should also take in five subject 
#marks of the students and find the total mark and 
#percentage. Display a result in such a way that their name, class,  and percentage are printed.

#solution

name = input("Enter the name: ")
student_class = input("Enter the class: ")

total = 0
# Taking marks of 5 subjects using loop

for i in range (1, 6): 
#loop it give 1,2,3,4,5. only not include 6
 marks = int(input(f"Enter the marks of subject {i}: "))
 total = total +  marks

# Calculating percentage
percentage = total / 5
# Displaying result

print("\n----- RESULT -----")
print("Name :", name)
print("Class :", student_class)
print("Total Marks :", total)
print("Percentage :", percentage, "%")