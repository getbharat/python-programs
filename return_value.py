user_input = input("Enter number of days you want to convert to hours\n")


def number_of_hours(days):
    local_hours = days * 24
    return local_hours


hours = number_of_hours(int(user_input))
print(f"Number of hours in {user_input} days {hours}")
