import itertools

class Patient:
    newid = itertools.count()
    def __init__(self, fName, sName, age, address):
        self.__firstName = fName
        self.__secondName = sName
        self.__age = age
        self.__doc = "Unassigned"
        self.__appointments = []
        self.__patientID = str(next(self.newid))+"-p"

    def get_firstName(self):
        return self.__firstName
    def set_firstName(self, newFirstName):
        self.__firstName = newFirstName
    def get_secondName(self):
        return self.__secondName
    def set_secondName(self, newSecondName):
        self.__secondName = newSecondName
    def get_age(self):
        return self.__age
    def set_age(self, newAge):
        self.__age = newAge
    def get_doc(self):
        return self.__doc
    def set_doc(self, newDoc):
        self.__doc = newDoc
    def get_pID(self):
        return self.__patientID
    
    def __str__(self) :
        return f'{self.__firstName:<10}{self.__secondName:<10}|{self.__doc:^15}|{self.__patientID:^5}'

#testing
def main():
    pat1 = Patient("Arthur", "Allen", 23, "Kuwait")
    print(pat1)
    pat2 = Patient("Nathaniel", "Herrera", 42, "UK")
    pat2.set_doc("Dr Lukas")
    print(pat2)
    print("Patient 2's age is: " + str(pat2.get_age()))

if __name__ == "__main__":
    main()