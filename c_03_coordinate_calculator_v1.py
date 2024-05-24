import math


def split_values(question, max_values=4, remove=None):
    while 1:
        response = input(question)
        int_coordinates = []
        try:
            if remove is None:
                remove = {"(", ")", " "}
            for remove_char in remove:
                response = str.replace(response, remove_char, "")
            response = str.split(response, ",")

            # check if int and check if anything else than numbers if it is a string it catches the error and asks again
            for coord in response:
                int_coordinates.append(float(coord))
            if len(response) == max_values:
                break

        except ValueError:
            print("Please input 2 valid coordinates\n")
            continue
        print("To many coordinates! please input 2 coordinates (2 coordinates == 4 values)\n")

    return int_coordinates


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
