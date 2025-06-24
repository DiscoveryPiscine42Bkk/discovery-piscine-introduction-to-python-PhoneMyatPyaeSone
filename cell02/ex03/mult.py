first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
result = int(first_num) * int(second_num)

if result > 0:
    print(first_num, "*", second_num, "=", result)
    print("The result is positive.")
elif result < 0:
    print(first_num, "*", second_num, "=", result)
    print("The result is negative.")
else: 
    print(first_num, "*", second_num, "=", result)
    print("The result is both positive and negative.")