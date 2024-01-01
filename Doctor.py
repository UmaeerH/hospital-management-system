class Doctor:
    def __init__(self, fName, sName, speciality):
        self.__firstName = fName
        self.__secondName = sName
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

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
    

    def add_patient(self, patient):
        self.patients.append(patient)

    def __str__(self) :
        return f'{self.__firstName:<10}{self.__secondName:<10}|{self.__speciality:^15}'
    
# testing
doc1 = Doctor("Umi", "Fudge", "Scientist")
doc2 = Doctor("Tokai", "Teio", "Horse Vet")
print(doc1)
print(doc2)
doc2.set_speciality("Retired")
print(doc2)