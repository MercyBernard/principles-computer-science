#Receive user input and format month to string and day to integer
month = str(input("Please enter the month: "))
day = int(input("Please enter the day: "))

#Create a condition for Month between March to June, March inclusive
if month == 'March' or month == 'April' or month == 'May':
    if month == 'March':
        if 20 <= day <= 31: #Check dates between 19 to 31 in March
            print(f"{month} {day} is autumn in the southern hemisphere.")  
        else:
            print(f"{month} {day} is summer in the southern hemisphere.")
    else:
        print(f"{month} {day} is autumn in the southern hemisphere.")

elif month == "June" or month == 'July' or month == 'August':
    if month == 'June':
        if 21 <= day <= 31: #Check dates between 20 to 31 in June
            print(f"{month} {day} is winter in the southern hemisphere.")
        else:
            print(f"{month} {day} is autumn in the southern hemisphere.")
    else:
        print(f"{month} {day} is winter in the southern hemisphere.")
        
elif month == 'September' or month == 'October' or month == 'November':
    if month == 'September':
        if 22 <= day <= 31: #Check dates between 21 to 31 in September
            print(f"{month} {day} is spring in the southern hemisphere.")
        else:
            print(f"{month} {day} is winter in the southern hemisphere.")
    else:
        print(f"{month} {day} is spring in the southern hemisphere.")
        
elif month == 'December' or month == 'January' or month == 'February':
    if month == 'December':
        if 21 <= day <= 31: #Check dates between 20 to 31 in December
            print(f"{month} {day} is summer in the southern hemisphere.")
        else:
            print(f"{month} {day} is spring in the southern hemisphere.")
    else:
        print(f"{month} {day} is summer in the southern hemisphere.")