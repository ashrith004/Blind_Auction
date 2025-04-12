print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         [_________]
                     
                         `'-------'`
                       .-------------.
                      [_______________]
              
    ''')

def find_highest_bidder(biding_dictionary):
    winner =""
    highest_bid = 0
    for bidder in biding_dictionary:
        bid_amount = biding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid =bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of $ {highest_bid}")       
        
bids ={}
continue_bidding = True
while continue_bidding:
    names = input("Please enter your name ?  ")
    price = int(input("What is your bid ?   $"))
    bids[names] = price
    should_continue = input("Are there any other bidders ?? Type 'Yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" *100)  
