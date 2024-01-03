import tkinter
from tkinter import ttk
import itertools

from Admin import Admin
from Doctor import Doctor
from Patient import Patient

#ACTORS
admins = [Admin('admin','123','B1 1AB'), Admin('admin2','242','B2 1AB')] # username is 'admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
discharged_patients = []

class loginGUI:
    def __init__(self):
        self.mw = tkinter.Tk()
        #styling
        self.mw.geometry("300x200")
        self.mw.resizable(0,0)
        self.mw.title("Hospital Log-in")
        self.mw.configure(bg="#d6d4ff")
        #frames
        self.topFrame = tkinter.Frame(self.mw, background="#d6d4ff")
        self.midFrame = tkinter.Frame(self.mw, background="#d6d4ff")
        self.botFrame = tkinter.Frame(self.mw, background="#d6d4ff")
        self.topFrame.pack(side="top")
        self.midFrame.pack(side="top")
        self.botFrame.pack(side="top")
        #Buttons

        self.adminButton = tkinter.Button(self.topFrame, text="ADMIN", command=self.adminLogPage, background="#69bad1")
        self.adminButton.pack(side="top")
        self.adminButton.grid(row=0, column=1, padx=10, pady=5)

        self.doctorButton = tkinter.Button(self.midFrame, text="DOCTOR", command=self.docPage, background="#69bad1")
        self.doctorButton.pack(side="left")
        self.doctorButton.grid(row=0, column=1, padx=10, pady=5)

        self.patientButton = tkinter.Button(self.botFrame, text="PATIENT", command=self.patPage, background="#69bad1")
        self.patientButton.pack(side="left")
        self.patientButton.grid(row=0, column=1, padx=10, pady=5)
        tkinter.mainloop()


    def adminLogPage(self):
        #window properties
        self.window = tkinter.Toplevel()
        self.window.title("Admin Log-in")
        self.window.geometry("400x250")
        self.window.resizable(0,0)
        self.window.configure(bg="#d6d4ff")
        #frames
        self.window.topAdminLogFrame = tkinter.Frame(self.window)
        self.window.midAdminLogFrame = tkinter.Frame(self.window)
        self.window.botAdminLogFrame = tkinter.Frame(self.window)
        self.window.topAdminLogFrame.pack(side="top")
        self.window.midAdminLogFrame.pack(side="top")
        self.window.botAdminLogFrame.pack(side="top")
        #Input
        self.window.userLabel = tkinter.Label(self.window.topAdminLogFrame, text="Username: ", bg="#d6d4ff")
        self.window.userLabel.pack(side="left")
        self.window.enterUser = tkinter.Entry(self.window.topAdminLogFrame, width=14, bg="#d4d4d4")
        self.window.enterUser.pack(side="left")
        self.window.passLabel = tkinter.Label(self.window.midAdminLogFrame, text="Password: ", bg="#d6d4ff")
        self.window.passLabel.pack(side="left")
        self.window.enterPass = tkinter.Entry(self.window.midAdminLogFrame, width=14, bg="#d4d4d4")
        self.window.enterPass.pack(side="left")
        self.window.logButton = tkinter.Button(self.window.botAdminLogFrame, text="Log-in", bg="#d4d4d4", command=self.attempted)
        self.window.logButton.pack(side="bottom")

        
    def attempted(self):
        enteredUser = self.window.enterUser.get() 
        enteredPass = self.window.enterPass.get()
        print("Login button was clicked")
        for i in range(len(admins)):
            if enteredUser == admins[i].get_userName() and enteredPass == admins[i].get_pass():
                print("Login verified")
                break
            else:
                print("Checking again..")
                
            

        


    def docPage(self):
        print("WIP DOC")

    def patPage(self):
        print("WIP PATIENT")


def main():
    newUI = loginGUI()

if __name__ == "__main__":
    main()
