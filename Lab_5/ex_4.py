# Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like Manager, Engineer,
# and Salesperson. Each subclass should have attributes like salary and methods related to their roles.


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"{self.employee_id}: {self.name}"

class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id)
        self.salary = salary
        self.team_size = team_size

    def display_info(self):
        return f"Manager - {super().display_info()}, Salary: ${self.salary}, Team Size: {self.team_size}"

    def conduct_meeting(self):
        return f"{self.name} is conducting a meeting."

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        return f"Engineer - {super().display_info()}, Salary: ${self.salary}, Programming Language: {self.programming_language}"

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_language}."

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        return f"Salesperson - {super().display_info()}, Salary: ${self.salary}, Sales Target: ${self.sales_target}"

    def make_sale(self):
        return f"{self.name} made a sale worth ${self.sales_target}."


print("\n")
manager = Manager(name="John Manager", employee_id="M001", salary=80000, team_size=10)
print(manager.display_info())
print(manager.conduct_meeting())

print("\n")

engineer = Engineer(name="Alice Engineer", employee_id="E001", salary=70000, programming_language="Python")
print(engineer.display_info())
print(engineer.write_code())

print("\n")

salesperson = Salesperson(name="Bob Salesperson", employee_id="S001", salary=60000, sales_target=50000)
print(salesperson.display_info())
print(salesperson.make_sale())
