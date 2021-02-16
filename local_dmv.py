

class ChicagoDMV():
    def __init__(self):
        self.employees = set()
    
    def move_line(self, licence_type):
        for employee in self.employees:
            if employee.specialty == licence_type:
                employee.process_licence(licence_type)

    def list_employees(self):
        for employee in self.employees:
            print(employee.name)
    
    def add_employee(self, employee):
        self.employees.add(employee)