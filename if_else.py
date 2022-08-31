user_input = input("Enter Number of Days that you want to convert to hours\n")
numer_of_days = int(user_input)


def convert_to_hours(days):
    print(days)
    if days > 0:
        return f"Number of hours for {days} are {days * 24}"
    else:
        return f"Wrong input!"


print(convert_to_hours(numer_of_days))
