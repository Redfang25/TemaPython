from employee import Employee
# valeanu = 7 litere => x%3 = 1
# valeanu octavian tudor = 20 => Y/3 = 6
class Manager(Employee):
    mgr_count = 0
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = "A08." + department
        Manager.mgr_count += 1

    # valeanu = 7 litere => x%3 = 1
    # valeanu octavian tudor = 20 => Y/3 = 6
    def display_employee(self):
        print(f"Salariu este {self.salary}")


alpha = Manager("Alex", 200, "HR")
Beta = Manager("Troy", 250, "resources")
Gamma = Manager("Terry", 200, "IT")
Delta = Manager("Jimothy", 150, "sales")
dead = Manager("ME", 2000, "reception")

alpha.display_employee()
Beta.display_employee()
Gamma.display_employee()
Delta.display_employee()
dead.display_employee()
#print(dead.mgr_count)

print(f"{alpha.empCount}")
print(f"{alpha.mgr_count}")