# (Q-1) Create a CSV file for address book, CSV file should have column for name, address,
# mobile, email. Insert 2-3 dummy data entered by user.



import csv

data = []

n = int(input("How many records you want to enter: "))

for i in range(n):
    print(f"\nEnter details for person {i+1}")

    name = input("Enter Name: ")
    address = input("Enter Address: ")
    mobile = input("Enter Mobile Number: ")
    email = input("Enter Email: ")

    data.append([name, address, mobile, email])

with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Address", "Mobile", "Email"])

    writer.writerows(data)

print("\nData saved successfully in address_book.csv")