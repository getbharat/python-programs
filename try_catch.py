user_input = input("Enter the number of days that you want to convert to hours\n")


def convert_to_hours(days):
    try:
        days_to_int = int(days)
        if days_to_int > 0:
            if days_to_int == 0:
                print(f"Number of day can't be zero")
            else:
                print(f"Number of hours for {days} are {days_to_int * 24}")
    except ValueError:
        print("Wrong input!")


convert_to_hours(user_input)