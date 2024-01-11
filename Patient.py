import itertools

class Patient:
    newid = itertools.count()
    def __init__(self, fName, sName, age, number="None provided", address="None provided", doc="Unassigned", illness="no diagnosis", appointment=[]):
        self.__firstName = fName
        self.__secondName = sName
        self.__age = age
        self.__number = number
        self.__address = address
        self.__doc = doc
        self.__illness = illness
        self.__appointments = appointment
        self.__patientID = str(next(self.newid))+"-p"

    def get_firstName(self):
        return self.__firstName
    def set_firstName(self, newFirstName):
        self.__firstName = newFirstName
    def get_secondName(self):
        return self.__secondName
    def set_secondName(self, newSecondName):
        self.__secondName = newSecondName
    def get_fullpName(self):
        namestr = str(self.__firstName) + " " + str(self.__secondName) 
        return namestr

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
    
    def get_illess(self):
        return self.__illness
    def set_illness(self, diag):
        self.__illness = diag
        
    def get_numb(self):
        return self.__number
    def set_numb(self, number):
        self.__number = str(number)
    
    def add_appointment(self, date):
        self.__appointments.append(date)
    def rem_appointment(self, date):
        self.__appointments.remove(date)

    def get_address(self):
        return self.__address
    def set_address(self, nAdd):
        self.__address = nAdd
    
    def display(self) :
        return f'{self.__firstName:<10}{self.__secondName:<10}|{self.__doc:^15}|{self.__patientID:^5}'
    
    def __str__(self):
        return f'{self.__firstName} {self.__secondName}, {self.__age} | Treated by {self.__doc} for {self.__illness} | ID: {self.__patientID}\nAddress: {self.__address} | numb: {self.__number}'

#testing
def main():
    pat1 = Patient("Arthur", "Allen", 23, "Kuwait")
    print(pat1.display())
    pat2 = Patient("Nathan", "Herrera", 42, "UK")
    pat2.set_doc("Dr Lukas")
    print(pat2.display())

    pat3 = Patient("Marie", "Norris", 32, "52 whatever road")
    pat3.set_doc("Dr Hellen")
    pat3.set_numb("01215728952")
    print(pat3)

if __name__ == "__main__":
    main()