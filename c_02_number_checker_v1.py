def int_checker(question, error="Please enter a number above 0", exit_code=None):
    while True:
        print()
        response = input(f"\n{question}").lower()
        if response == exit_code:
            return response
        try:
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print("This is not a number", error)


while True:
    questions = int_checker("How many calculations do you need to calculate (inf for endless)",
                            "Please enter a number above 0 (inf for endless)",
                            "inf")
    if questions != "inf":
        print("You chose", questions, "Questions")
    else:
        print("You chose endless")
