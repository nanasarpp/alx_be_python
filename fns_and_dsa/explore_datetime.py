from datetime import datetime, timedelta 
# from datetime import timedelta
current_date = ""
def display_current_datetime():
    current_date = datetime.now()
    # return current_date
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    future_date = datetime.now() + timedelta(days=number_of_days)
    # return future_date
    print(f"Future date: {future_date}")
calculate_future_date()
display_current_datetime()
