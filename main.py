seconds = input('Enter the number of seconds (integer): ')
seconds = int(seconds)

# ... complete the code below

seconds = divmod(seconds,3600)
hours = seconds[0]
seconds = divmod(seconds[1],60)
minutes = seconds[0]
seconds = seconds[1]


# Follow the formatting given
# e.g. The duration is X hours, X minutes, and X seconds.
print("The duration is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
