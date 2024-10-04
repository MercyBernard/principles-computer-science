menu = {
    "Hot Dog" : 1.50,
    "Slice of Pizza" : 1.99,
    "Whole Pizza" : 9.95,
    "Soft Drink" : 0.59
}

num_hot_dogs = int(input("Please enter number of Hot Dogs: "))
num_pizza_slices = int(input("Please enter number of Pizza slices: "))
num_whole_pizzas = int(input("Please enter number of Whole Pizzas: "))
num_soft_drinks = int(input("Please enter number of Soft Drinks: "))

total_hot_dogs = num_hot_dogs * menu["Hot Dog"]
total_pizza_slices = num_pizza_slices * menu["Slice of Pizza"]
total_whole_pizza = num_whole_pizzas * menu["Whole Pizza"]
total_soft_drinks = num_soft_drinks * menu["Soft Drink"]

total_cost = total_hot_dogs + total_pizza_slices + total_whole_pizza + total_soft_drinks

print(f"The total cost of the order is ${total_cost:.2f}")
