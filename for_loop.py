def validate_and_execute():
    try:
        days = int(input_element)
        if days > 0:
            return f"Number of hours for {input_element} days are {24 * days}"
        elif days == 0:
            return f"Number of days can't be 0"
        else:
            return f"Number of days can't be in minus"
    except ValueError:
        print("Invalid input!")


user_input = ""
while user_input != "exit":
    user_input = input("Enter the list of days to convert in hours\n")
    for input_element in user_input.split(","):
        print(validate_and_execute())
