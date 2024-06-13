def agree(question):
    while True:
        reply = input(question).lower()
        if reply in ("yes", "no", "n", "y"):
            # This will return True is the first letter of the response is "y" OR False
            return reply[0] == 'y' and True or False
        # it will reach this warning if it did not return
        print("Reply yes/no")


while True:
    if agree("Do you want to see the instructions"):
        print("{Instructions}\n")
