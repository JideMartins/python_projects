bid = {}


def auction():
    # declare variable for continuing bid
    continue_bid = True
    while continue_bid:

        # Ask for inputs
        name = input("Enter your name:\n")
        price = int(input("Enter your bidding price:\n$ "))

        # populate bid
        bid[name] = price

        # check if there are other bidders
        other_bidders = input(
            "Are there other bidders? Type \"y\" for yes and \"n\" for no: ").lower()

        if other_bidders == "n":
            continue_bid = False
        elif other_bidders == "y":
            continue
        else:
            print("please type the appropriate response: \"y\" for yes and \"n\" for no: ")
            other_bidders

# run function
auction()

# Get max price and key
max_name = max(bid, key=bid.get)
max_price = max(bid.values())

# convert bid values to list
max_count = list(bid.values()).count(max_price)

if max_count >= 2:
    # state the value and run the silent auction again
    print(f"The maximum bid is tied, we would have to start all over\nFeel free to change your bid price")
    # run function again
    auction()
elif max_count==1:
    print(f"The winner is {max_name} with a bid of ${max_price}")
    # return bid

