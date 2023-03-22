total_distance = int(input())
spent_fuel = float(input())

avg_consumption = total_distance /spent_fuel
avg_consumption = "{:.3f}".format(avg_consumption)

print(avg_consumption, "km/l")