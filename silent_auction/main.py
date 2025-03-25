from gavel import logo

print(logo)

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
    other_bidders = input(
        "Are there other bidders? Type \"y\" for yes and \"n\" for no: ").lower()

    if other_bidders == "n":
        continue_bid = False

    # print(bid)


# Get max price and key
max_name = max(bid, key=bid.get)
max_price = max(bid.values())

print(f"The winner is {max_name} with a bid of ${max_price}")
