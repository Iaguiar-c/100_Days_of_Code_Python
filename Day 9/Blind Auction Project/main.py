import art

print(art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
continue_bidding = True
bids = {}

def find_highest_bid(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} wich a bid of ${highest_bid}")

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    for bid in bids:
        bids[name] = price
        if should_continue == "no":
            continue_bidding = False
            find_highest_bid(bids)
        if should_continue == "yes":
            print("\n" * 100)
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

