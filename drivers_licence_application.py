class DriversLicenceApplication:

    def __init__(self, name, licence_type):
        self.name = name 
        self.licence_type = licence_type
        self.double_checked = False

    def double_check_form(self):
        self.double_checked = True
    
    def submit_application(self, local_dmv):
        if self.double_checked:
            local_dmv.move_line(self.licence_type)
        else:
            print("Please double-check your form first")