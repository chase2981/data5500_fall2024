import os
from collections import deque

# Get the current directory of this file
curr_dir = os.path.dirname(__file__)

tkr = "AAPL"
stock_fil = curr_dir + "/" + tkr + ".txt" # Build the file path

# Open the file
file = open(stock_fil, "r")

# Initialize the deque with a max length of 5 (for 5 days of prices)
prices = deque(maxlen=5)

days = 5
buy = 0
profit = 0.0

# Read the first 5 prices to fill the deque initially
for i in range(days):
    prices.append(float(file.readline().strip()))

# Process the remaining prices
for line in file:
    p = float(line.strip())  # Read the next price
    avg = sum(prices) / days  # Calculate the moving average

    # Perform trading strategy
    if p > avg and buy == 0:  # Buy
        print("buying at:", p)
        buy = p
    elif p < avg and buy != 0:  # Sell
        print("selling at:", p)
        profit += p - buy
        print("trade profit:", p - buy)
        buy = 0
    else:
        pass  # Do nothing, just monitor

    # Add the new price to the deque, which automatically removes the oldest price
    prices.append(p)

# Close the file
file.close()

# Print the final profit and percentage returns
print("profit:", profit)
print("percentage returns%:", 100 * (profit / prices[0]))

input("press enter")
