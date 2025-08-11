from datetime import datetime, timedelta 
# from datetime import timedelta
current_date = ""
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # return current_date
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    future_date = datetime.now() + timedelta(days = number_of_days)
    formated_future = future_date.strftime("%Y-%m-%d")
    # return future_date
    print(f"Future date: {formated_future}")

display_current_datetime()
calculate_future_date()
