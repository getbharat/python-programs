user_input = input("Enter number to know sum of its digits\n")
input_to_int = int(user_input)


def sum_of_numbers(number):
    sum_of_nums = 0
    while number > 0:
        remainder = number % 10
        number = int(number / 10)
        sum_of_nums = sum_of_nums + remainder

    return f"Sum of the digits of {input_to_int} is {sum_of_nums}"


print(sum_of_numbers(int(user_input)))
