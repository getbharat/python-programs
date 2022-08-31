user_input = input("Enter number to get factorial\n")


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


return_value = factorial(int(user_input))

print(f"Factorial of {user_input} is {return_value}")
