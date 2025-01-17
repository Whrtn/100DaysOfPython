from os import system

system("cls")
print("Welcome to the secret auction program.")
auction_complete = False
bids = {}

while not auction_complete:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no':").lower()
    if more_bidders == "no":
        auction_complete = True
    elif more_bidders == "yes":
        system("cls")
    else:
        print("Invalid selection")
        auction_complete = True

winning_bid = 0
for key in bids:
    if bids[key] > winning_bid:
        winning_bid = bids[key]
        winner_string = f"The winner is {key} with a bid of ${bids[key]}"

print(winner_string)
