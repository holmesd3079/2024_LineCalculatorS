import math
from datetime import date

import pandas


# Yes/no checker, but it returns true for yes and false for no
def agree(question):
    while 1:
        reply = input(question).lower()
        if reply in {"yes", "no", "n", "y"}:
            return reply[0] == 'y' and True or False
        print("Reply yes/no")


def calculate_cords(x1, y1, x2, y2):
    # Calculate all the axis to all the formula's
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    # if the x equals to 0 which is not able to be calculated, instead returns undefined
    gradient = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 'undefined'

    # if the gradient isint able to be solved it will return only the x equation else the y and x together if it is.
    equation = (f"x = {x1}" if gradient == 'undefined' else f"y = {gradient:.2f}x + {y1 - gradient * x1:.2f}")

    # Return all the calculated data back
    return [distance, midpoint, gradient, equation]


# Used to split comma separated values into tables/arrays
def split_values(question, max_values=4, exit_code=None, remove=("(", ")", " ")):
    # Leaves loop until the values input is meeting the expected
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        processed_cords = []
        try:
            for remove_char in remove:
                response = str.replace(response, remove_char, "")
            response = str.split(response, ",")
            # check if int and check if anything else than numbers if it is a string it catches the error and asks again
            for coord in response:
                processed_cords.append(float(coord))

            if len(response) == max_values:
                matches = 0
                for i in range(4):
                    if processed_cords[0] == processed_cords[i]:
                        matches += 1
                if matches == 4:
                    print("This is a dot/point, please try something valid")
                    continue
                break

        except ValueError:
            print("Please input 2 valid coordinates\n")
            continue
        print(("Not enough coordinates!" if len(response) < max_values else "To many coordinates!")
              + " please input 2 coordinates (2 coordinates == 4 values)\n")

    return processed_cords


# check if the response is an integer, returns if it is
def int_checker(question, error="Please enter a number above 0", exit_code=None):
    while True:

        response = input(question).lower()
        if response == exit_code:
            return response
        try:
            response = int(response)
            if response > 0:
                return response
        except ValueError:
            print(error)


all_coordinates, distances, midpoints, gradients, equations = [], [], [], [], []

if agree("Do you want to see the instructions"):
    print("instructions\n"
          "'xxx' to quit (during coordinate input)\n"
          "\n - Input the amount of questions you need to calculate ('inf' for endless)"
          "\n - When the program asks you for your values '1,2,3,4' or (1,2), (3,4)"
          "\n - (SPACES ARE IGNORED) - comma separated")

max_loops = int_checker("\nHow many questions are you going to calculate ('inf for endless')", exit_code="inf")
max_loops = max_loops == "inf" and -1 or max_loops
loops_count = 0

# MAIN ROUTINE
while max_loops != loops_count:
    coordinate_table = []  # [x1 y2 x1 y2] format
    coordinate_response = split_values("('xxx' to quit)\n"
                                       "Please input your Coordinates 'x, y, x, y' or (x, y), (x, y):", exit_code="xxx")
    # If exit code is the response
    if coordinate_response == "xxx":
        # If loops_count is 0 (nothing) it will restart the loop, else it will exit the loop if above 0
        if not loops_count:
            print("You need to calculate least 1 equation before quiting!\n")
            continue
        break

    _x1, _y1, _x2, _y2 = coordinate_response
    answer_table = calculate_cords(_x1, _y1, _x2, _y2)
    print(
        f"\n",
        f"Coordinates:\t({_x1}, {_y1}), ({_x2},{_y2})\n",
        f"Distance:\t{answer_table[0]:.2f}\n",
        f"Midpoint:\t{answer_table[1]}\n",
        f"Gradient:\t{answer_table[2]}\n",
        f"Equation:\t{answer_table[3]}\n"
    )
    # Add all data to the tables for the dictionary
    all_coordinates.append(f"({_x1}, {_y1}), ({_x2}, {_y2})")
    distances.append(answer_table[0])
    midpoints.append(answer_table[1])
    gradients.append(answer_table[2])
    equations.append(answer_table[3])

    loops_count += 1

# create dictionary
coord_calculator_dic = {
    "Coordinates": all_coordinates,
    "Distance": distances,
    "Midpoint": midpoints,
    "Gradient": gradients,
    "Equation": equations
}
# File name / date
today = date.today()
sh_date = f"{today.day}_{today.month}_{today.year}"
filename = f"C_CALC_{sh_date}"

# Setup dataframe (Pandas)
coord_calculator_frame = pandas.DataFrame(coord_calculator_dic)
coord_calculator_frame = coord_calculator_frame.set_index('Equation')
coordinates_string = pandas.DataFrame.to_string(coord_calculator_frame)

# Set filename and set save file
to_write = f" ---- Coordinate calculator answer Data {sh_date} ----\n\n {coordinates_string}"
text_file = open(f"{filename}.txt", "w+")
text_file.write(to_write)
text_file.close()

print("\n\n\n")
print(to_write)
