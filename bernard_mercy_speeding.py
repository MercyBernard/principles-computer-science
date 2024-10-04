speed_limit = int(input('Please enter the speed limit for the road: '))
driving_speed = int(input("Please enter the vehicle's recorded speed: "))

#Calculate speed difference
speed_diff = driving_speed - speed_limit

#Place conditions
if speed_diff <= -10:
    print('The speeding fine is $50.')

elif 6 <= speed_diff <= 20:
    print('The speeding fine is $75.')

elif 21 <= speed_diff <= 40:
    print('The speeding fine is $150.')

elif speed_diff > 40:
    print('The speeding fine is $300.')

else:
    print('There is no fine.')