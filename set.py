user_input = ""
while user_input != "exit":
    user_input = input("Enter the values that you want in set\n ")
    list_of_days = user_input.split(",")
    print(type(list_of_days))
    for days in list_of_days:
        try:
            day_in_int = int(days)
            if day_in_int > 0:
                print(day_in_int * 24)
        except ValueError:
            print("Wrong Input!")

    print(type(set(list_of_days)))
    for days in set(list_of_days):
        try:
            day_in_int = int(days)
            if day_in_int > 0:
                print(day_in_int * 24)
        except ValueError:
            print("Wrong Input!")
