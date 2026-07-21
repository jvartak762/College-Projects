# Smart Energy Consumption Calculator

units =  float(input("Enter the number of electricity units consumed: "))
cost_per_unit = 8
total_cost = units * cost_per_unit
print("--------------------------------")
print("        Bill Summary            ")
print("--------------------------------")
print("Total units consumed: ", units)
print("Cost per unit:    Rs. ", cost_per_unit)
print("Total cost:       Rs. ", total_cost)
