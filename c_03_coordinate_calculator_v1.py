import math


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


# returns [Distance, Midpoint, Gradient, Equation]
def calculate_cords(x1, y1, x2, y2):
    # Calculate all the axis to all the formula's
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    # if the x equals to 0 which is not able to be calculated, instead returns undefined
    gradient = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 'undefined'
    # if the gradient isint able to be solved it will return only the x equation else the y and x together if it is.
    equation = (f"x = {x1}" if gradient == 'undefined' else f"y = {gradient:.2f}x + {y1 - gradient * x1:.2f}")
    # Return all the data back
    return [f"Distance:\t{distance:.2f}",
            f"Midpoint:\t{midpoint}",
            f"Gradient:\t{gradient}",
            f"Equation:\t{equation}"]


while True:
    print()
    coordinates = split_values("Input Coordinates 'x, y, x, y' or (x, y), (x, y):")
    print(coordinates)
    print()

    _x1, _y1, _x2, _y2 = coordinates
    for items in calculate_cords(_x1, _y1, _x2, _y2):
        print(items)
