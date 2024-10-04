phone_num = int(input("Please enter your phone number: "))

area_code = phone_num // 10000000 #This is used to remove the right most 7 digits

line = phone_num % 10000000 #To get the rightmost 7 digits

prefix = line // 10000

line_num = phone_num % 10000
print()

print(f"Phone Number: ({area_code}) {prefix}-{line_num}")

