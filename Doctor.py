import itertools
from Patient import Patient

class Doctor:
    newid = itertools.count()
    def __init__(self, fName, sName, speciality="None", address="None provided", numb="None provided", pats=[], apps=[]):
        self.__firstName = fName
        self.__secondName = sName
        self.__speciality = speciality
        self.__address = address
        self.__number = numb
        self.__patients = pats
        self.__appointments = apps
        self.__docID = str(next(self.newid))+"-d"

    def get_firstName(self):
        return self.__firstName
    def set_firstName(self, newFirstName):
        self.__firstName = newFirstName

    def get_secondName(self):
        return self.__secondName
    def set_secondName(self, newSecondName):
        self.__secondName = newSecondName

    def get_fullName(self):
        namestr = str(self.__firstName) + " " + str(self.__secondName) 
        return namestr

    def get_speciality(self):
        return self.__speciality
    def set_speciality(self, newSpec):
        self.__speciality = newSpec

    def get_docID(self):
        return self.__docID

    def get_numb(self):
        return self.__number
    def set_numb(self, number):
        self.__number = str(number)

    def get_address(self):
        return self.__address
    def set_address(self, newAdd):
        self.__address = newAdd

    def get_patient(self):
        return self.__patients
    def add_patient(self, patient):
        self.__patients.append(patient)
    def remove_patient(self, patient):
        self.__patients.remove(patient)
    def get_patientString(self):
        if len(self.__patients) != 0:
            patList = ""
            for i in range(len(self.__patients)):
                patList += f'{self.__patients[i].get_fullpName():<20} | ID:  {self.__patients[i].get_pID()}\n'
            return patList.strip()
        else:
            return "No Patients"

    def get_appointment(self):
        return self.__appointments
    def add_appointment(self, date):
        self.__appointments.append(date)
    def rem_appointment(self, date):
        self.__appointments.remove(date)

    def __str__(self) :
        return f'{self.__firstName:<10}{self.__secondName:<10}|{self.__speciality:^15}|{self.__docID:^5}'
    
# testing
def main():
    doc1 = Doctor("Ruby", "Armstrong", "Scientist")
    doc2 = Doctor("Timothy", "Lopez", "GP")
    doc2.set_speciality("Retired")
    doc3 = Doctor("Francis", "Mathis", "Radiologist")
    doc4 = Doctor("Darrell", "Baldwin")
    print("---------------------------------------")
    print("{0}\n{1}\n{2}\n{3}".format(doc1, doc2, doc3, doc4))
    print("---------------------------------------")
    print(doc4.get_fullName())

if __name__ == "__main__":
    main()