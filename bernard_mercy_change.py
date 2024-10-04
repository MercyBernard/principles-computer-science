cents = int(input('Please enter a number of cents: '))

quarters = cents // 25 
quarter_remainder = cents % 25

dimes = quarter_remainder // 10
dimes_remainder = quarter_remainder % 10

nickels = dimes_remainder // 5
nickels_remainder = dimes_remainder % 5

pennies = nickels_remainder // 1
pennies_remainder = nickels_remainder % 1

print(f"Coins: {quarters} quarters, {dimes} dimes, {nickels} nickels and {pennies} pennies")