spent_time = int(input())
avg_speed = int(input())

distance = spent_time * avg_speed
fuel_spent = distance / 12
fuel_spent = "{:.3f}".format(fuel_spent)

print(fuel_spent)