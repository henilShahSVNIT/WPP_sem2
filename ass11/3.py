'''After accidentally leaving an ice chest of fish and shrimp in your car for a week while you
were on vacation, you're now in the market for a new vehicle. Your insurance didn't cover
the loss, so you want to make sure you get a good deal on your new car.
Given a Series of car asking_prices and another Series of car fair_prices, determine which
cars for sale are a good deal. In other words, identify cars whose asking price is less than
their fair price.
The result should be a list of integer indices corresponding to the good deals
in asking_prices.'''

import pandas as pd

asking_prices_input = input("Enter the asking prices of the cars (comma-separated): ")
fair_prices_input = input("Enter the fair prices of the cars (comma-separated): ")

asking_prices = pd.Series([int(i) for i in asking_prices_input.split(',')])
fair_prices = pd.Series([int(i) for i in fair_prices_input.split(',')])

good_deals = asking_prices < fair_prices

good_deals_indices = good_deals.index[good_deals].tolist()

print("Good deals found at indices:", good_deals_indices)