from funcyion import salary, hello_who
name = "Max"
salary(2,10)
hello_who(name)
print(salary(2,10))
if salary(2,10) != 20:
    print("Error")
if hello_who("Max") != "Hello, Max":
    print("Error")
else:
    print("Good")
if hello_who("Leo") != "Hello, Leo":
    print("Error")
else:
    print("Good")