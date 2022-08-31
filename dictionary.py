def convert_days_to_unit(days, unit):
    if str(unit).lower() == "hours":
        print(f"Number of {unit} {days * 24} in {days} days")
    elif str(unit).lower() == "minutes":
        print(f"Number of {unit} {days * 24 * 60} in {days} days")
    elif str(unit).lower() == "seconds":
        print(f"Number of {unit} {days * 24 * 60 * 60} in {days} days")
    else:
        print("Unsupported Unit")


def validate_and_execute():
    try:
        days = int(days_and_unit_dictionary["days"])
        if days == 0:
            print("Days can't be zero")
        elif days > 0:
            convert_days_to_unit(days, days_and_unit_dictionary["unit"])
        else:
            print("Number of days can't be negative")
    except ValueError:
        print("Invalid input")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days conversion unit\n")
    number_of_days_and_unit = user_input.split(":")
    print(number_of_days_and_unit)
    days_and_unit_dictionary = {"days": number_of_days_and_unit[0], "unit": number_of_days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()