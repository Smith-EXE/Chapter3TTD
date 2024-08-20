# Ethan Smith 08/20/2024 Chapter 3 Things to do

# 3.1 How many seconds are in an hour? 
# Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).
# 3.2 Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.

secondsInMinute = 60
minutesInHour = 60

secondsInHour = secondsInMinute * minutesInHour

print("There are", secondsInHour, "seconds in an hour!")

# 3.3 How many seconds are in a day? Use your seconds_per_hour variable.
# 3.4 Calculate seconds per day again, but this time save the result in a variable called seconds_per_day.

secondsInDay = secondsInHour * 24

print("There are", secondsInDay, "seconds in a day!")

# 3.5 Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.

HoursInDayFP = secondsInDay/secondsInHour

print("There are", HoursInDayFP, "Hours in a day!")

# 3.6 Divide seconds_per_day by seconds_per_hour, using integer (//) division. 
# Did this number agree with the floating-point value from the previous question, aside from the final .0?

HoursInDayID = secondsInDay//secondsInHour

print("There are", HoursInDayID, "Hours in a day!")

# The value retrieved from Integer division did agree with the value retrieved by floating-point division.