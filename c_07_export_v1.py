import pandas
import random
from datetime import date

today = date.today()
sh_date = f"{today.day}_{today.month}_{today.year}"
filename = f"C_CALC_{sh_date}"

print(filename)

# Lists for pandas columns

all_coordinates = [f"({1}, {2}), ({3}, {4})", f"({5}, {6}), ({7}, {8})", f"({9}, {10}), ({11}, {12})",
                   f"({13}, {14}), ({15}, {16})", f"({17}, {18}), ({19}, {20})"]
distances = [2.82, 2.82, 2.82, 2.82, 2.82]
midpoints = [f"{2}, {3}", f"{6}, {7}", f"{10}, {11}", f"{14}, {15}", f"{18}, {19}"]
gradient = [1, 1, 1, 1, 1]

coord_calculator_dic = {
    "Equation": all_coordinates,
    "Distance": distances,
    "Midpoint": midpoints,
    "Gradient": gradient
}

coord_calculator_frame = pandas.DataFrame(coord_calculator_dic)

coord_calculator_frame = coord_calculator_frame.set_index('Equation')

mini_movie_string = pandas.DataFrame.to_string(coord_calculator_frame)

print("\n\n\n")
to_write = f" ---- Coordinate calculator answer Data {filename} ----\n\n {mini_movie_string}"

print(to_write)

text_file = open(f"{filename}.txt", "w+")

text_file.write(to_write)
text_file.close()
