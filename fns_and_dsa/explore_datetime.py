from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time in "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in "YYYY-MM-DD"
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date
    try:
        # Prompt the user to enter a number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
