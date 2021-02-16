from drivers_licence_application import DriversLicenceApplication
from local_dmv import ChicagoDMV
from dmv_employee import DmvEmployee




if __name__ == "__main__" :
    bobsLicence = DriversLicenceApplication("Bob", "regular")
    janesLicence = DriversLicenceApplication("Jane", "regular")
    billyBadassLicence = DriversLicenceApplication("Billy A. Badass", "motorcycle")

    # print(bobsLicence.licence_type, janesLicence.licence_type, billyBadassLicence.licence_type)

    barb = DmvEmployee("Barb", "regular")
    babs = DmvEmployee("Babs", "commercial")
    bertha = DmvEmployee("Bertha", "motorcycle")


    chiDmv = ChicagoDMV()
    chiDmv.add_employee(barb)
    chiDmv.add_employee(babs)
    chiDmv.add_employee(bertha)
    chiDmv.list_employees()
    print()

    janesLicence.double_check_form()
    janesLicence.submit_application(chiDmv)

    billyBadassLicence.submit_application(chiDmv)
    billyBadassLicence.double_check_form()
    billyBadassLicence.submit_application(chiDmv)