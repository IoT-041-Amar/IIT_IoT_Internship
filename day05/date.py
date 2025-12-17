# Import the datetime module
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Display the current date and time
print("Current date and time:", current_datetime)

# Get the day of the week (0 = Monday, 6 = Sunday)
day_of_week_index = current_datetime.weekday()

# List of days for easy reference
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print the day of the week
print("Day of the week:", days_of_week[day_of_week_index])