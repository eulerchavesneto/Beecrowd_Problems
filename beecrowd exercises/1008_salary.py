employee_number = int(input())
worked_hours = int(input())
received_per_hour = float(input())

salary = worked_hours * received_per_hour
salary = "{:.2f}".format(salary)

print("NUMBER =", employee_number)
print("SALARY = U$", salary)