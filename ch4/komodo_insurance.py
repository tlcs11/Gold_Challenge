badges = {}                    #string for a key and empty list for input
                 
while True:
    print("1 to make badge",
            "3 to print all badges", "2 to edit a badge")
    op = input("> ")
    if op == "1":
        b_id = int(input("enter en id:"))
        add_door = input("Add a door to badge Y or N:  ")
        badges.update({b_id:[]})
        input("Add a door to badge Y or N:  ")
        if add_door in ["Y", "y"]:
            b_doors = input("Door Num: " )
            badges[b_id].append(b_doors)
    if op == "2":
        b_id = int(input("Enter badge id:"))
        remove_door = input("ARE YOU SURE YOU WOULD LIKE TO REMOVE ACCESS?")
        badges.update({b_id:[NONE]})

    elif op == "3":
        print(badges)
    elif op == "4":
        exit()


