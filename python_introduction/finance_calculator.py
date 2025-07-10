#Taking input from the user
income = input("Enter your monthly income:")

expenses = input("Enter your total monthly expenses:")

#calculating the monthly savings 
monthly_savings = int(income) - int(expenses)

#Finding the simple interest on the savings 
projected_savings = monthly_savings*12 +int((monthly_savings*12*0.05))

#Displaying the result
print(f"Your monthly savings is ${monthly_savings}.")

print(f"Projected savings after one year, with interest, is: ${projected_savings}.")