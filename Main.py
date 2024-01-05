import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont  
import itertools
#Class imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
#ACTORS
admins = [Admin('admin','123','B1 1AB'), Admin('admin2','242','B2 1AB')] # username is 'admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
discharged_patients = []

class loginGUI:
    #INITIAL WINDOW
    def __init__(self):
        self.mw = tk.Tk()
        #styling
        self.mw.geometry("300x200")
        self.mw.resizable(0,0)
        self.mw.title("Hospital Log-in")
        self.mw.configure(bg="#d6d4ff")
        #frames
        self.topFrame = tk.Frame(self.mw, background="#d6d4ff")
        self.midFrame = tk.Frame(self.mw, background="#d6d4ff")
        self.botFrame = tk.Frame(self.mw, background="#d6d4ff")
        self.topFrame.pack(side="top")
        self.midFrame.pack(side="top")
        self.botFrame.pack(side="top")
        #Buttons

        self.adminButton = tk.Button(self.topFrame, text="ADMIN", command=self.adminLogPage, background="#69bad1")
        self.adminButton.pack(side="top")
        self.adminButton.grid(row=0, column=1, padx=10, pady=5)

        self.doctorButton = tk.Button(self.midFrame, text="DOCTOR", command=self.docPage, background="#69bad1")
        self.doctorButton.pack(side="left")
        self.doctorButton.grid(row=0, column=1, padx=10, pady=5)

        self.patientButton = tk.Button(self.botFrame, text="PATIENT", command=self.patPage, background="#69bad1")
        self.patientButton.pack(side="left")
        self.patientButton.grid(row=0, column=1, padx=10, pady=5)
        tk.mainloop()

    #WINDOW FOR ADMIN LOGIN
    def adminLogPage(self):
        #window properties
        self.window = tk.Toplevel()
        self.window.title("Admin Log-in")
        self.window.geometry("400x250")
        self.window.resizable(0,0)
        self.window.configure(bg="#d6d4ff")
        #frames
        self.window.topAdminLogFrame = tk.Frame(self.window)
        self.window.midAdminLogFrame = tk.Frame(self.window)
        self.window.botAdminLogFrame = tk.Frame(self.window)
        self.window.topAdminLogFrame.pack(side="top")
        self.window.midAdminLogFrame.pack(side="top")
        self.window.botAdminLogFrame.pack(side="top")
        #Input
        self.window.userLabel = tk.Label(self.window.topAdminLogFrame, text="Username: ", bg="#d6d4ff")
        self.window.userLabel.pack(side="left")
        self.window.enterUser = tk.Entry(self.window.topAdminLogFrame, width=14, bg="#d4d4d4")
        self.window.enterUser.pack(side="left")
        self.window.passLabel = tk.Label(self.window.midAdminLogFrame, text="Password: ", bg="#d6d4ff")
        self.window.passLabel.pack(side="left")
        self.window.enterPass = tk.Entry(self.window.midAdminLogFrame, width=14, bg="#d4d4d4")
        self.window.enterPass.pack(side="left")
        self.window.logButton = tk.Button(self.window.botAdminLogFrame, text="Log-in", bg="#d4d4d4", command=self.attempted)
        self.window.logButton.pack(side="bottom")

    #WINDOW FOR ADMIN
    def adminPage(self):
        self.adWindow = tk.Toplevel()
        self.adWindow.title("Admin Home")
        self.adWindow.geometry("500x350")
        self.adWindow.resizable(0,0)
        self.adWindow.configure(bg="#d6d4ff")
        #frames
        self.adWindow.topAdminFrame = tk.Frame(self.adWindow, background="#d6d4ff")
        self.adWindow.midAdminFrame = tk.Frame(self.adWindow, background="#d6d4ff")
        self.adWindow.botAdminFrame = tk.Frame(self.adWindow, background="#d6d4ff")
        self.adWindow.bot2AdminFrame = tk.Frame(self.adWindow, background="#d6d4ff")
        self.adWindow.topAdminFrame.pack(side="top")
        self.adWindow.midAdminFrame.pack(side="top")
        self.adWindow.botAdminFrame.pack(side="top")
        self.adWindow.bot2AdminFrame.pack(side="top")
        #Content
        self.adWindow.header = tk.Label(self.adWindow.topAdminFrame, text="Admin View", background="#d6d4ff", font=tkfont.Font(family='Helvetica', size=18, weight="bold"))
        self.adWindow.header.pack(side="top")
        self.adWindow.docButton = tk.Button(self.adWindow.midAdminFrame, text="View Doctors", bg="#d4d4d4", command=self.attempted)     #Placeholder commands
        self.adWindow.docButton.pack(side="left")
        self.adWindow.docButton.grid(row=0, column=2, padx=10, pady=5)
        self.adWindow.patButton = tk.Button(self.adWindow.botAdminFrame, text="View Patients", bg="#d4d4d4", command=self.attempted)        #Placeholder commands
        self.adWindow.patButton.pack(side="left")
        self.adWindow.patButton.grid(row=0, column=2, padx=10, pady=5)
        self.adWindow.reportButton = tk.Button(self.adWindow.bot2AdminFrame, text="Management Report", bg="#d4d4d4", command=self.attempted)        #Placeholder commands
        self.adWindow.reportButton.pack(side="left")
        self.adWindow.reportButton.grid(row=0, column=2, padx=10, pady=5)


    def attempted(self):
        try:
            enteredUser = self.window.enterUser.get() 
            enteredPass = self.window.enterPass.get()
            print("Login button was clicked")
            for i in range(len(admins)):
                if enteredUser == admins[i].get_userName() and enteredPass == admins[i].get_pass():
                    print("Login verified")
                    self.adminPage()
                    break
                else:
                    print("Checking again..")
        except:
            print("Admin already logged in")


    def docPage(self):
        print("WIP DOC")

    def patPage(self):
        print("WIP PATIENT")


def main():
    newUI = loginGUI()

if __name__ == "__main__":
    main()
