# Blind Auction Program
from replit import clear
import art
 
print(art.logo)
print("Welcome to Blind Aucation Program:\n")
bids = {}
biding_finished = False
winner = ""
def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not biding_finished:
    name = input("What is yor name?")
    price = int(input("What is your bid? $"))
    bids[name] = price
    print(bids)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        biding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
 