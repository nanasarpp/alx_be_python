#Taking input from the user
monthly_income = int(input("Enter your monthly income:"))

monthly_expenses = int(input("Enter your total monthly expenses:"))

#calculating the monthly savings 
monthly_savings = monthly_income - monthly_expenses

#Finding the simple interest on the savings 
projected_savings = monthly_savings*12 +int((monthly_savings*12*0.05))

#Displaying the result
print(f"Your monthly savings are ${monthly_savings}.")

print(f"Projected savings after one year, with interest, is: ${projected_savings}.")