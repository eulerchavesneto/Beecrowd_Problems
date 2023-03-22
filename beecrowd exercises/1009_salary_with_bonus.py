name = (input())
salary = float(input())
total_sales = float(input())

bonus = total_sales * 15/100
bonus_salary = salary + bonus
bonus_salary = "{:.2f}".format(bonus_salary)

print("TOTAL = R$", bonus_salary)

