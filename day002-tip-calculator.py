# In this lesson I learned about the most common data types in python. I also learned how to use mathematics.
# Lastly I learned that f-print allows us to print different data types as strings, helping to shorten code.

print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill?"))
percentage_tip = int(input("What percentage would you like to tip?"))
number_of_people = int(input("How many people are splitting the bill?"))
each_pay = ((percentage_tip / 100 * total_bill ) + total_bill) / number_of_people
print(f"Each person should pay: ${each_pay}")