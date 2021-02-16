

class DmvEmployee:

    def __init__(self, name, specialty):
        self.name = name 
        self.specialty = specialty

    def process_licence(self, licence_type):
        print(f"Your {licence_type} application has been processed by {self.name}")