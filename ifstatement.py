my_num = int(input("Enter a number:  "))

if my_num % 2 == 0:
    print(f"{my_num} is even number")
else:
    print(f"{my_num} is odd number")

my_age = int(input("Enter your age:"))
if my_age < 18:
    print(f"{my_age} cannot vote ")
else:
    print(f"{my_age} can vote ")
