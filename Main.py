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
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Will','Robinson','Pediatrics'), Doctor('Jone','Carlos','Cardiology'), Doctor("Irie", "Ford", "Pediatrics", "B1 1AB", "+4472794272")]
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
        self.adWindow.docButton = tk.Button(self.adWindow.midAdminFrame, text="View Doctors", bg="#d4d4d4", command=self.adminDocPage) 
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


    def adminDocPage(self):
        self.adDocWindow = tk.Toplevel()
        self.adDocWindow.title("View Doctors")
        self.adDocWindow.geometry("500x450")
        self.adDocWindow.resizable(0,0)
        self.adDocWindow.configure(bg="#ffa7a7")
        #Frames
        self.adDocWindow.topFrame = tk.Frame(self.adDocWindow, background="#ffa7a7")
        self.adDocWindow.midFrame = tk.Frame(self.adDocWindow, background="#ffa7a7")
        self.adDocWindow.mid2Frame = tk.Frame(self.adDocWindow, background="#ffa7a7")
        self.adDocWindow.botFrame = tk.Frame(self.adDocWindow, background="#a7a7a7")
        self.adDocWindow.topFrame.pack(side="top")
        self.adDocWindow.midFrame.pack(side="top")
        self.adDocWindow.mid2Frame.pack(side="top")
        self.adDocWindow.botFrame.pack(side="top")
        #Variables
        displayName = "None selected"
        displayID = "None"
        displaySpec = " "
        displayNumb = " "
        displayAdd = " "
        displayPatients = " "
        #Content
        self.adDocWindow.docList = tk.Listbox(self.adDocWindow.topFrame, background="#ff9797", width=30)
        self.adDocWindow.docList.pack(side="left")
        self.adDocWindow.docList.grid(row=0, column=1, padx=10, pady=5)
        for i in range(len(doctors)):           #List generation
            self.adDocWindow.docList.insert(i+1, doctors[i].get_fullName())
        self.adDocWindow.showButton = tk.Button(self.adDocWindow.midFrame, text='Show Doc info', command=self.docInfoDisp, background="#ff9797")
        self.adDocWindow.showButton.pack(side="left")
        self.adDocWindow.editButton = tk.Button(self.adDocWindow.midFrame, text="Edit Doc info", command=self.adminDocEdit, background="#ff9797")
        self.adDocWindow.editButton.pack(side="left")
        self.adDocWindow.delButton = tk.Button(self.adDocWindow.midFrame, text="Add Doctor", command=self.adminDocCreate, background="#a7c194")
        self.adDocWindow.delButton.pack(side="left")
        self.adDocWindow.docLabel = tk.Label(self.adDocWindow.mid2Frame, text="Doctor\'s Details", font=tkfont.Font(family='Helvetica', size=14, weight="bold"), background="#ffa7a7")
        self.adDocWindow.docLabel.pack(side="top")
        #DETAILS
        self.adDocWindow.docName = tk.Label(self.adDocWindow.botFrame, text=displayName, width=25, background="#a7a7a7")
        self.adDocWindow.docName.pack(side="top", expand="False")
        self.adDocWindow.docID = tk.Label(self.adDocWindow.botFrame, text=displayID, width=25, background="#a7a7a7")
        self.adDocWindow.docID.pack(side="top", expand="False")        
        self.adDocWindow.docSpec = tk.Label(self.adDocWindow.botFrame, text=displaySpec, width=25, background="#a7a7a7")
        self.adDocWindow.docSpec.pack(side="top", expand="False")
        self.adDocWindow.docNumb = tk.Label(self.adDocWindow.botFrame, text=displayNumb, width=25, background="#a7a7a7")
        self.adDocWindow.docNumb.pack(side="top", expand="False")
        self.adDocWindow.docAddress = tk.Label(self.adDocWindow.botFrame, text=displayAdd, width=35, background="#a7a7a7")
        self.adDocWindow.docAddress.pack(side="top", expand="False")
        self.adDocWindow.docPats = tk.Label(self.adDocWindow.botFrame, text=displayPatients, width=35, background="#a7a7a7")
        self.adDocWindow.docPats.pack(side="top", expand="True")
    
    def docInfoDisp(self):
        for i in self.adDocWindow.docList.curselection():
            varA = f'{"Name:":>10} {doctors[i].get_fullName():>15}'
            varB = f'{"ID:":>10} {doctors[i].get_docID():>15}'
            varC = f'{"Speciality:":>10} {doctors[i].get_speciality():>15}'
            varD = f'{"Number:":>10} {doctors[i].get_numb():>15}'
            varE = f'{"Address:":>10} {doctors[i].get_address():>25}'
            varF = f'{"Patients:":>10} {str(doctors[i].get_patient()):>25}'
            self.adDocWindow.docName.config(text=varA)
            self.adDocWindow.docID.config(text=varB)
            self.adDocWindow.docSpec.config(text=varC)
            self.adDocWindow.docNumb.config(text=varD)
            self.adDocWindow.docAddress.config(text=varE)
            self.adDocWindow.docPats.config(text=varF)
            
    def adminDocEdit(self):
        #get doc
        for i in self.adDocWindow.docList.curselection():
            selectedDoc = i
        #Window settings
        self.adDocEditWindow = tk.Toplevel()
        self.adDocEditWindow.title(doctors[selectedDoc].get_fullName())
        self.adDocEditWindow.geometry("300x250")
        self.adDocEditWindow.resizable(0,0)
        self.adDocEditWindow.configure(bg="#ffa7a7")

    def adminDocCreate(self):
        #Window
        self.adDocCreateWindow = tk.Toplevel()
        self.adDocCreateWindow.title("Create Doctor")
        self.adDocCreateWindow.geometry("300x350")
        self.adDocCreateWindow.resizable(0,0)
        self.adDocCreateWindow.configure(bg="#a7c194")
        #Frames
        self.adDocCreateWindow.nameFrame = tk.Frame(self.adDocCreateWindow, background="#a7c194")
        self.adDocCreateWindow.nameFrame.pack(side="top")
        self.adDocCreateWindow.surnameFrame = tk.Frame(self.adDocCreateWindow, background="#a7c194")
        self.adDocCreateWindow.surnameFrame.pack(side="top")
        self.adDocCreateWindow.specFrame = tk.Frame(self.adDocCreateWindow, background="#a7c194")
        self.adDocCreateWindow.specFrame.pack(side="top")
        self.adDocCreateWindow.botFrame = tk.Frame(self.adDocCreateWindow, background="#a7c194")
        self.adDocCreateWindow.botFrame.pack(side="top")
        #Inputs
        self.adDocCreateWindow.nameL = tk.Label(self.adDocCreateWindow.nameFrame, text="First name:")
        self.adDocCreateWindow.nameL.pack(side="left")
        self.adDocCreateWindow.nameE = tk.Entry(self.adDocCreateWindow.nameFrame, background="#d4d4d4")
        self.adDocCreateWindow.nameE.pack(side="left")
        self.adDocCreateWindow.surnameL = tk.Label(self.adDocCreateWindow.surnameFrame, text="Second name:")
        self.adDocCreateWindow.surnameL.pack(side="left")
        self.adDocCreateWindow.surnameE = tk.Entry(self.adDocCreateWindow.surnameFrame, background="#d4d4d4")
        self.adDocCreateWindow.surnameE.pack(side="left")
        self.adDocCreateWindow.specialityL = tk.Label(self.adDocCreateWindow.specFrame, text="Speciality:")
        self.adDocCreateWindow.specialityL.pack(side="left")
        self.adDocCreateWindow.specialityE = tk.Entry(self.adDocCreateWindow.specFrame, background="#d4d4d4")
        self.adDocCreateWindow.specialityE.pack(side="left")
        self.adDocCreateWindow.createButton = tk.Button(self.adDocCreateWindow.botFrame, text="Create Doctor", command=self.doctorCreate, background="#d4d4d4")
        self.adDocCreateWindow.createButton.pack(side="left")


    def doctorCreate(self):
        #Get
        enteredName = self.adDocCreateWindow.nameE.get()
        enteredSname = self.adDocCreateWindow.surnameE.get()
        enteredSpec = self.adDocCreateWindow.specialityE.get()
        try:
            new_doc = Doctor(enteredName, enteredSname, enteredSpec)
            doctors.append(new_doc)
        except:
            print("Error creating doctor")
        else:
            self.adDocWindow.docList.delete(0, len(doctors))
            for i in range(len(doctors)):           #List update
                self.adDocWindow.docList.insert(i+1, doctors[i].get_fullName())

    def docPage(self):
        #window properties
        self.docLogWindow = tk.Toplevel()
        self.docLogWindow.title("Doctor Log-in")
        self.docLogWindow.geometry("250x250")
        self.docLogWindow.resizable(0,0)
        self.docLogWindow.configure(bg="#58f9bb")
        #frames
        self.docLogWindow.topDocLogFrame = tk.Frame(self.docLogWindow)
        self.docLogWindow.midDocLogFrame = tk.Frame(self.docLogWindow)
        self.docLogWindow.botDocLogFrame = tk.Frame(self.docLogWindow)
        self.docLogWindow.topDocLogFrame.pack(side="top")
        self.docLogWindow.midDocLogFrame.pack(side="top")
        self.docLogWindow.botDocLogFrame.pack(side="top")
        #Input
        self.docLogWindow.idLabel = tk.Label(self.docLogWindow.topDocLogFrame, text="Enter your ID: ", bg="#58f9bb")
        self.docLogWindow.idLabel.pack(side="left")
        self.docLogWindow.enterID = tk.Entry(self.docLogWindow.topDocLogFrame, width=14, bg="#1dd48e")
        self.docLogWindow.enterID.pack(side="left")
        self.docLogWindow.logButton = tk.Button(self.docLogWindow.botDocLogFrame, text="Log-in", bg="#1dd48e", command=self.attempted) #Placeholder command
        self.docLogWindow.logButton.pack(side="bottom")

    def patPage(self):
        print("WIP PATIENT")


def main():
    loginGUI()

if __name__ == "__main__":
    main()
