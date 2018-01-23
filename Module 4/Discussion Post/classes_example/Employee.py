class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{0}.{1}@company.com".format(first, last)

    def fullName(self):
        return "{0} {1}".format(self.first, self.last)



emp_1 = Employee("Eric", "Zorn", 100000)
emp_2 = Employee("Richard", "Zorn", 500000)


print(emp_1.email)
print(emp_2.email)

print(emp_1.fullName())
print(emp_2.fullName())


# Employee.fullName(emp_1)
# Employee.fullName(emp_2)