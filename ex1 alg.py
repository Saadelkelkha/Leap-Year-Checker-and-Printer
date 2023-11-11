def is_leap_year(a):
    # Check if the year 'a' is divisible evenly by 400
    if a % 400 == 0:
        # If divisible by 400, it is a leap year
        return True
    else:
        # If not divisible by 400, it is not a leap year
        return False

def leap_years_between(start_year):
    # Iterate over a 100-year range starting from the specified 'start_year'
    for i in range(start_year, start_year + 100):
        # Check if the current year 'i' is a leap year using the is_leap_year function
        if is_leap_year(i) == True:
            # If it's a leap year, print a message indicating so
            print(i, "is a leap year.")

start_year=int(input("type the start year"))

# Call the leap_years_between function with a starting year 
leap_years_between(start_year)
