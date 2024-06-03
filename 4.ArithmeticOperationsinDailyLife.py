# 4. Arithmetic Operations in Daily Life
# Objective: The aim of this assignment is to get familiarized with basic arithmetic operations and understand how they can be applied in everyday situations.

"""
Task 1: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic
"""
price_of_bread = 5
price_of_peanuts = 10
price_of_jelly = 15
price_total  = price_of_bread + price_of_peanuts + price_of_jelly
print("total is: " , price_total)

# Task 2: Bank Interest (Extra Credit) If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.
saving_account = 10000
interest_rate = 7/100
#After one year
saving_account += saving_account*interest_rate 

print("saving account after one year: ", saving_account)