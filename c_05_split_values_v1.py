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


coordinates = split_values("Input Coordinates 'x, y, x, y' or (x, y), (x, y):")

print(coordinates, "Are your coordinates")
