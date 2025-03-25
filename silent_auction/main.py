bid = {}


# declare variable for continuing bid
continue_bid = True

while continue_bid:

    # Ask for inputs
    name = input("Enter your name:\n")
    price = int(input("Enter your bidding price:\n$ "))

    # populate bid
    bid[name] = price

    # check if there are other bidders
    other_bidders = input("Are there other bidders? Type \"y\" for yes and \"n\" for no: ").lower()

    if other_bidders == "n":
        continue_bid = False
    
    print(bid)


