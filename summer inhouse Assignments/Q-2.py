#Q-2 Input 2 strings concatinate them and store in another variable. then perform 
# generally used string methods on it like lower(), upper(), title(), swapcase(), capitalize(), 
# casefold(), center(), count(), endswith(), find(), isalnum(), isdigit(), isnumeric(), isspace(), replace()


# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Concatenate strings dono string add hongi 
result = str1 + " " + str2
print("\nConcatenated String:", result)

print("Lower Case:", result.lower())
print("Upper Case:", result.upper())
print("Title Case:", result.title())
print("Swap Case:", result.swapcase())
print("Capitalize:", result.capitalize())
print("Casefold:", result.casefold())
print("Center:", result.center(30, "*"))
print("Count of 'a':", result.count("a"))
print("Ends with 'n':", result.endswith("n"))
print("Find 'o':", result.find("o"))
print("Is Alnum:", result.isalnum()) #isalnum() check karta hai:✅ String mai sirf alphabets (A-Z, a-z) numbers (0-9) hone chahiye. Space ya special character nahi hona chahiye.
print("Is Digit:", result.isdigit()) #Check karta hai: 👉 String mai sirf digits hain ya nahi.
print("Is Numeric:", result.isnumeric()) #Check karta hai:👉 String numeric value hai ya nahi. Yeh isdigit() jaisa hi hota hai mostly.
print("Is Space:", result.isspace())#Check karta hai: 👉 String mai sirf spaces hain ya nahi
print("Replace:", result.replace("a", "@"))