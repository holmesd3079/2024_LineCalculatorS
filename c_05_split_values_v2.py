def split_values(question, max_values=4, exit_code=None, remove=("(", ")", " ")):
    # Leaves loop until the values input is meeting the expected
    while True:
        response = input(question).lower()
        # if response exit code
        if response == exit_code:
            return response
        processed_cords = []
        # Error catching, restart if something is incorrect, ie All points are the same number or input is not a number
        try:
            # Remove unneeded characters from string
            for remove_char in remove:
                response = str.replace(response, remove_char, "")
            # Turn response into table of the comma split response
            response = str.split(response, ",")
            # Check if is int & check if anything else than numbers if it is a string it catches the error & asks again
            for coord in response:
                processed_cords.append(float(coord))
            # Checks if it matches max values (since 2 points need 4 coordinates)
            if len(response) == max_values:
                matches = 0
                # Making sure the numbers given are all not the same
                for i in range(max_values):
                    if processed_cords[0] == processed_cords[i]:
                        matches += 1
                if matches == 4:
                    print("This is a dot/point, please try something valid")
                    continue
                break

        # Error catching - if something on the table errors (like a letter) it will notify the user
        except ValueError:
            print("Please input 2 valid coordinates\n")
            continue
        # Tells the user if they have put in too many coordinates or too little
        print(("Not enough coordinates!" if len(response) < max_values else "To many coordinates!")
              + " please input 2 coordinates (2 coordinates == 4 values)\n")

    return processed_cords


coordinates = split_values("('xxx' to quit)\n"
                           "Please input your Coordinates 'x, y, x, y' or (x, y), (x, y): ",
                           exit_code="xxx")

print("You have quit" if coordinates == "xxx" else str(coordinates) + " Are your coordinates")
