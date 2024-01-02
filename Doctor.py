import itertools

class Doctor:
    newid = itertools.count()
    def __init__(self, fName, sName, speciality):
        self.__firstName = fName
        self.__secondName = sName
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []
        self.__docID = str(next(self.newid))+"-d"

    def get_firstName(self):
        return self.__firstName
    def set_firstName(self, newFirstName):
        self.__firstName = newFirstName
    def get_secondName(self):
        return self.__secondName
    def set_secondName(self, newSecondName):
        self.__secondName = newSecondName
    def get_speciality(self):
        return self.__speciality
    def set_speciality(self, newSpec):
        self.__speciality = newSpec
    def get_docID(self):
        return self.__docID

    def add_patient(self, patient):
        self.__patients.append(patient)

    def add_appointment(self, date):
        self.__appointments.append(date)

    def __str__(self) :
        return f'{self.__firstName:<10}{self.__secondName:<10}|{self.__speciality:^15}|{self.__docID:^5}'
    
# testing
def main():
    doc1 = Doctor("Ruby", "Armstrong", "Scientist")
    doc2 = Doctor("Timothy", "Lopez", "GP")
    doc2.set_speciality("Retired")
    doc3 = Doctor("Francisco", "Mathis", "Radiologist")
    print("---------------------------------------")
    print("{0}\n{1}\n{2}".format(doc1, doc2, doc3))
    print("---------------------------------------")

if __name__ == "__main__":
    main()