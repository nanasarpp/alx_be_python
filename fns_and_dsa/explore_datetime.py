from datetime import datetime, timedelta 
# from datetime import timedelta

current_dateTime = datetime.now()

print(f"Current date and time: {current_dateTime}")

number_of_days = int(input("Enter the number of days to add to the current date: "))

Future_date = current_dateTime + timedelta(days=number_of_days)
print(f"Future date: {Future_date}")