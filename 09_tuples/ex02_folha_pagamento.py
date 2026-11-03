# Exercise 02 — Payroll
#
# HR needs the tax deduction and net salary from a single payroll calculation.
# Create calculate_payroll, which receives the gross salary and returns two values: the 10% tax deduction and the net salary (gross salary minus deduction).
# Call the function with a salary of R$ 5,000 and unpack the return value.
# Display: "Deduction: R$[value] | Net salary: R$[value]".

# Your solution:

def calculate_payroll(salary):
  deduction = salary * 0.10
  net_salary = salary - deduction
  return net_salary, deduction

net_salary, deduction = calculate_payroll(5000)
print(f"Deduction: R${deduction:.2f} | Net salary: R${net_salary:.2f}")
