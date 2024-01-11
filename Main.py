import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont  
import itertools
import copy
import csv
import sys
#Class imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
#ACTORS
admins = [Admin('admin','123','B1 1AB'), Admin('admin2','242','B2 1AB')] # username is 'admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Will','Robinson','Pediatrics'), Doctor('Jone','Carlos','Cardiology'), Doctor("Irie", "Ford", "Pediatrics", "B1 1AB", "+4472794272")]
patients = []
discharged_patients = []
loggedDoc = 0

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

        self.doctorButton = tk.Button(self.midFrame, text="DOCTOR", command=self.docLogPage, background="#69bad1")
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
        self.window.botAdminLogFrame = tk.Frame(self.window, background="#d6d4ff")
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
        self.window.logButton.pack(side="top")
        self.window.textLabel = tk.Label(self.window.botAdminLogFrame, text="Case sensitive", bg="#d6d4ff", font=tkfont.Font(family='Helvetica', size=8))
        self.window.textLabel.pack(side="top")

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
        self.adWindow.header.grid(pady=5)
        self.adWindow.docButton = tk.Button(self.adWindow.midAdminFrame, text="View Doctors", bg="#d4d4d4", command=self.adminDocPage) 
        self.adWindow.docButton.pack(side="left")
        self.adWindow.docButton.grid(row=1, column=1, padx=10, pady=2)
        self.adWindow.patButton = tk.Button(self.adWindow.botAdminFrame, text="View Patients", bg="#d4d4d4", command=self.adminPatPage)
        self.adWindow.patButton.grid(row=0, column=0, padx=6, pady=10)
        self.adWindow.dpatButton = tk.Button(self.adWindow.botAdminFrame, text="View Discharged", bg="#d4d4d4", command=self.adminDpatPage)
        self.adWindow.dpatButton.grid(row=0, column=1, padx=6, pady=10)
        self.adWindow.reportButton = tk.Button(self.adWindow.bot2AdminFrame, text="Management Report", bg="#d4d4d4", command=self.attempted)        #Placeholder commands
        self.adWindow.reportButton.grid(row=0, column=0, padx=6, pady=10)
        self.adWindow.editButton = tk.Button(self.adWindow.bot2AdminFrame, text="Account Details", bg="#d4d4d4", command=self.adminOwnPage)
        self.adWindow.editButton.grid(row=0, column=1, padx=6, pady=10)

    def attempted(self):
        try:
            enteredUser = self.window.enterUser.get() 
            enteredPass = self.window.enterPass.get()
            print("Login button was clicked")
            for i in range(len(admins)):
                if enteredUser == admins[i].get_userName() and enteredPass == admins[i].get_pass():
                    print("Login verified")
                    self.adminPage()
                    global loggedAdmin
                    loggedAdmin = admins[i]
                    global editingAdmin
                    editingAdmin = copy.deepcopy(admins[i])
                    global adminIndex
                    adminIndex = i
                    break
                else:
                    print("Checking again..")
        except:
            print("Admin already logged in")

    def adminOwnPage(self):
        global loggedAdmin
        self.adminWindow = tk.Toplevel()
        self.adminWindow.title(loggedAdmin.get_userName()+"'s Settings")
        self.adminWindow.geometry("250x300")
        self.adminWindow.resizable(0,0)
        self.adminWindow.configure(bg="#151730")
        #Frames
        self.adminWindow.frame1 = tk.Frame(self.adminWindow, background="#151730")
        self.adminWindow.frame2 = tk.Frame(self.adminWindow, background="#151730")
        self.adminWindow.frame3 = tk.Frame(self.adminWindow, background="#151730")
        self.adminWindow.frame4 = tk.Frame(self.adminWindow, background="#151730")
        self.adminWindow.frame5 = tk.Frame(self.adminWindow, background="#151730")
        self.adminWindow.frame1.pack(side="top")
        self.adminWindow.frame2.pack(side="top")
        self.adminWindow.frame3.pack(side="top")
        self.adminWindow.frame4.pack(side="top")
        self.adminWindow.frame5.pack(side="top")
        #Content
        self.adminWindow.userL = tk.Label(self.adminWindow.frame1, background="#151730", text=f"User: {loggedAdmin.get_userName():>10}", font=tkfont.Font(family='Helvetica', size=10, weight="bold"), fg='#c4dbff')
        self.adminWindow.userL.pack(side="left")
        self.adminWindow.passL = tk.Label(self.adminWindow.frame2, background="#151730", text=f"Pass: {loggedAdmin.get_pass():>10}", font=tkfont.Font(family='Helvetica', size=10, weight="bold"), fg='#c4dbff')
        self.adminWindow.passL.pack(side="left")
        self.adminWindow.addressL = tk.Label(self.adminWindow.frame3, background="#151730", text=f"Address: {loggedAdmin.get_address():>10}", font=tkfont.Font(family='Helvetica', size=10, weight="bold"), fg='#c4dbff')
        self.adminWindow.addressL.pack(side="left")
        self.adminWindow.entry = tk.Entry(self.adminWindow.frame4, background="#d3d3d3")
        self.adminWindow.entry.pack(side="top")
        self.adminWindow.entry.grid(row=1, column=1, padx=10, pady=10)
        self.adminWindow.setName = tk.Button(self.adminWindow.frame5, background="#d3d3d3", text="Set as Username", command=self.changeUser)
        self.adminWindow.setName.pack(side="top")
        self.adminWindow.setPass = tk.Button(self.adminWindow.frame5, background="#d3d3d3", text="Set as Password", command=self.changePass)
        self.adminWindow.setPass.pack(side="top")
        self.adminWindow.setAdd = tk.Button(self.adminWindow.frame5, background="#d3d3d3", text="Set as Address", command=self.changeAddress)
        self.adminWindow.setAdd.pack(side="top")

    def changeUser(self):
        editingAdmin.set_userName(self.adminWindow.entry.get())
        admins[adminIndex] = editingAdmin
        global loggedAdmin
        loggedAdmin = editingAdmin
        self.adminWindow.userL.config(text=f"User: {loggedAdmin.get_userName():>10}")

    def changePass(self):
        editingAdmin.set_pass(self.adminWindow.entry.get())
        admins[adminIndex] = editingAdmin
        global loggedAdmin
        loggedAdmin = editingAdmin
        self.adminWindow.passL.config(text=f"Pass: {loggedAdmin.get_pass():>10}")

    def changeAddress(self):
        editingAdmin.set_address(self.adminWindow.entry.get())
        admins[adminIndex] = editingAdmin
        global loggedAdmin
        loggedAdmin = editingAdmin    
        self.adminWindow.addressL.config(text=f"Address: {loggedAdmin.get_address():>10}")


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
            self.adDocWindow.docList.insert(i+1, f'{doctors[i].get_fullName()}  |  {doctors[i].get_docID()}')
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
            varF = f'{"Patients:":>10} \n{str(doctors[i].get_patientString()):>25}'
            self.adDocWindow.docName.config(text=varA)
            self.adDocWindow.docID.config(text=varB)
            self.adDocWindow.docSpec.config(text=varC)
            self.adDocWindow.docNumb.config(text=varD)
            self.adDocWindow.docAddress.config(text=varE)
            self.adDocWindow.docPats.config(text=varF)
            
    def adminDocEdit(self):
        #get doc
        for i in self.adDocWindow.docList.curselection():
            global selectedDoc
            selectedDoc = i
        global editingDoctor
        editingDoctor = copy.deepcopy(doctors[selectedDoc])
        #Window settings
        self.adDocEditWindow = tk.Toplevel()
        self.adDocEditWindow.title(editingDoctor.get_fullName())
        self.adDocEditWindow.geometry("300x250")
        self.adDocEditWindow.resizable(0,0)
        self.adDocEditWindow.configure(bg="#ffa7a7")
        #Frames
        self.adDocEditWindow.nameIDFrame = tk.Frame(self.adDocEditWindow, background="#ffa7a7")
        self.adDocEditWindow.specFrame = tk.Frame(self.adDocEditWindow, background="#ffa7a7")
        self.adDocEditWindow.addressFrame = tk.Frame(self.adDocEditWindow, background="#ffa7a7")
        self.adDocEditWindow.numbFrame = tk.Frame(self.adDocEditWindow, background="#ffa7a7")
        self.adDocEditWindow.alertFrame = tk.Frame(self.adDocEditWindow, background="#ffa7a7")
        self.adDocEditWindow.patFrame = tk.Frame(self.adDocEditWindow, background="#ffa7a7")
        self.adDocEditWindow.patFrame2 = tk.Frame(self.adDocEditWindow, background="#ffa7a7")
        self.adDocEditWindow.nameIDFrame.pack(side="top")
        self.adDocEditWindow.specFrame.pack(side="top")
        self.adDocEditWindow.addressFrame.pack(side="top")
        self.adDocEditWindow.numbFrame.pack(side="top")
        self.adDocEditWindow.alertFrame.pack(side="top")
        self.adDocEditWindow.patFrame.pack(side="top")
        self.adDocEditWindow.patFrame2.pack(side="top")
        #Content
        nameID = f'{editingDoctor.get_fullName():<15}|{editingDoctor.get_docID():^5}'
        self.adDocEditWindow.nameLab = tk.Label(self.adDocEditWindow.nameIDFrame, background="#ffa7a7", text=nameID, font=tkfont.Font(family='Helvetica', size=12, weight="bold"))
        self.adDocEditWindow.nameLab.pack(side="top")
        self.adDocEditWindow.entry = tk.Entry(self.adDocEditWindow.nameIDFrame, background="#d4d4d4")
        self.adDocEditWindow.entry.pack(side="top")
        #Buttons
        self.adDocEditWindow.specButton = tk.Button(self.adDocEditWindow.specFrame, background="#d4d4d4", text=f'{"Set as Specialisation":^20}', command=self.editSpec)
        self.adDocEditWindow.addButton = tk.Button(self.adDocEditWindow.addressFrame, background="#d4d4d4", text=f'{"Set as Address":^20}', command=self.editAdd)
        self.adDocEditWindow.numbButton = tk.Button(self.adDocEditWindow.numbFrame, background="#d4d4d4", text=f'{"Set as Number":^20}', command=self.editNumb)
        self.adDocEditWindow.specButton.pack(side="top")
        self.adDocEditWindow.addButton.pack(side="top")
        self.adDocEditWindow.numbButton.pack(side="top")
        #Alert
        self.adDocEditWindow.alertLabel = tk.Label(self.adDocEditWindow.alertFrame, background="#ffa7a7", text=" ", font=tkfont.Font(family='Helvetica', size=12, weight="bold"))
        self.adDocEditWindow.alertLabel.pack(side="top")
        #Patients
        self.adDocEditWindow.patEntryLab = tk.Label(self.adDocEditWindow.patFrame, background="#d4d4d4", text="PatientID:")
        self.adDocEditWindow.patEntryLab.pack(side="left")
        self.adDocEditWindow.patEntry = tk.Entry(self.adDocEditWindow.patFrame, background="#d4d4d4")
        self.adDocEditWindow.patEntry.pack(side="left")
        self.adDocEditWindow.patPlus = tk.Button(self.adDocEditWindow.patFrame, background="#d4d4d4", text="+", command=self.patientAdd)
        self.adDocEditWindow.patPlus.pack(side="right")
        self.adDocEditWindow.patRem = tk.Button(self.adDocEditWindow.patFrame, background="#d4d4d4", text="-", command=self.patientRemove)
        self.adDocEditWindow.patRem.pack(side="right")
        self.adDocEditWindow.patLabel = tk.Label(self.adDocEditWindow.patFrame2, background="#ffa7a7", text="Waiting for action", font=tkfont.Font(family='Helvetica', size=10, weight="bold"))
        self.adDocEditWindow.patLabel.pack(side="top")
    
    #Edit property functions
    def editSpec(self):
        editingDoctor.set_speciality(self.adDocEditWindow.entry.get())
        doctors[selectedDoc] = editingDoctor
        self.adDocEditWindow.alertLabel.config(text="Speciality Changed")
    def editAdd(self):
        editingDoctor.set_address(self.adDocEditWindow.entry.get())
        doctors[selectedDoc] = editingDoctor
        self.adDocEditWindow.alertLabel.config(text="Address Changed")
    def editNumb(self):
        editingDoctor.set_numb(self.adDocEditWindow.entry.get())
        doctors[selectedDoc] = editingDoctor
        self.adDocEditWindow.alertLabel.config(text="Number Changed")

    def patientAdd(self):
        enteredPat = self.adDocEditWindow.patEntry.get()
        for i in range(len(patients)):
            if enteredPat.lower() == patients[i].get_pID():
                print("Found patient")
                if patients[i].get_doc() != "Unassigned":
                    self.adDocEditWindow.patLabel.config(text=f"Patient already assigned to {patients[i].get_doc()}")
                else:
                    editingDoctor.add_patient(patients[i])
                    tempPat = copy.deepcopy(patients[i])
                    tempPat.set_doc(editingDoctor.get_docID())
                    patients[i] = tempPat
                    doctors[selectedDoc] = editingDoctor
                    self.adDocEditWindow.patLabel.config(text="Patient has been assigned")
                    print(patients[i])
                break
            else:
                self.adDocEditWindow.patLabel.config(text="Patient ID not found")

    def patientRemove(self):
        enteredPat = self.adDocEditWindow.patEntry.get()
        for i in range(len(editingDoctor.get_patient())):
            if enteredPat.lower() == patients[i].get_pID():
                print("Found patient")
                if patients[i].get_doc() == "Unassigned":
                    self.adDocEditWindow.patLabel.config(text="Patient already unassigned")
                elif patients[i].get_doc() == editingDoctor.get_docID():
                    tempPatRem = copy.deepcopy(patients[i])
                    editingDoctor.remove_patient(i)
                    tempPatRem.set_doc("Unassigned")
                    patients[i] = tempPatRem
                    doctors[selectedDoc] = editingDoctor
                    self.adDocEditWindow.patLabel.config(text="Patient has been unassigned")
                    print(patients[i])
                else:
                    self.adDocEditWindow.patLabel.config(text="Patient is with another doctor")
            else:
                self.adDocEditWindow.patLabel.config(text="Patient ID not found")

    def adminDocCreate(self):
        #Window
        self.adDocCreateWindow = tk.Toplevel()
        self.adDocCreateWindow.title("Create Doctor")
        self.adDocCreateWindow.geometry("300x150")
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
        self.adDocCreateWindow.createButton.pack(side="top")
        self.adDocCreateWindow.warningText = tk.Label(self.adDocCreateWindow.botFrame, text=" ", background="#a7c194", font=tkfont.Font(family='Helvetica', size=14, weight="bold"))
        self.adDocCreateWindow.warningText.pack(side="top")

    def doctorCreate(self):
        #Get Entered info
        enteredName = self.adDocCreateWindow.nameE.get().capitalize()
        enteredSname = self.adDocCreateWindow.surnameE.get().capitalize()
        enteredSpec = self.adDocCreateWindow.specialityE.get().capitalize()
        dupeCheck = False
        for i in range(len(doctors)):
            if enteredName == doctors[i].get_firstName() and enteredSname == doctors[i].get_secondName():
                print("Name taken")
                dupeCheck = True
                self.adDocCreateWindow.warningText.config(text="Name already taken")
                break
        if dupeCheck == False:
            try:
                new_doc = Doctor(enteredName, enteredSname, enteredSpec)
                doctors.append(new_doc)
            except:
                print("Error creating doctor")
            else:           #List update
                self.adDocWindow.docList.delete(0, len(doctors))
                self.adDocCreateWindow.warningText.config(text="Doctor Added")
                for i in range(len(doctors)):
                    self.adDocWindow.docList.insert(i+1, f'{doctors[i].get_fullName()}  |  {doctors[i].get_docID()}')

    def adminPatPage(self):
        self.adPatWindow = tk.Toplevel()
        self.adPatWindow.title("View Patients")
        self.adPatWindow.geometry("500x450")
        self.adPatWindow.resizable(0,0)
        self.adPatWindow.configure(bg="#aab9e6")
        #Frames
        self.adPatWindow.topFrame = tk.Frame(self.adPatWindow, background="#aab9e6")
        self.adPatWindow.midFrame = tk.Frame(self.adPatWindow, background="#aab9e6")
        self.adPatWindow.mid1Frame = tk.Frame(self.adPatWindow, background="#aab9e6")
        self.adPatWindow.mid2Frame = tk.Frame(self.adPatWindow, background="#aab9e6")
        self.adPatWindow.botFrame = tk.Frame(self.adPatWindow, background="#a7a7a7")
        self.adPatWindow.topFrame.pack(side="top")
        self.adPatWindow.midFrame.pack(side="top")
        self.adPatWindow.mid1Frame.pack(side="top")
        self.adPatWindow.mid2Frame.pack(side="top")
        self.adPatWindow.botFrame.pack(side="top")
        #Content
        self.adPatWindow.patList = tk.Listbox(self.adPatWindow.topFrame, background="#a7b0c9", width=30)
        self.adPatWindow.patList.pack(side="left")
        self.adPatWindow.patList.grid(row=0, column=1, padx=10, pady=5)
        for i in range(len(patients)):           #List generation
            self.adPatWindow.patList.insert(i+1, f'{patients[i].get_fullpName()}  |  {patients[i].get_pID()}')
        self.adPatWindow.showButton = tk.Button(self.adPatWindow.midFrame, text='Show Patient info', command=self.patInfoDisp, background="#a7a7a7")
        self.adPatWindow.showButton.pack(side="left")
        self.adPatWindow.editButton = tk.Button(self.adPatWindow.midFrame, text="Edit Patient info", command=self.adminPatEdit, background="#a7a7a7")
        self.adPatWindow.editButton.pack(side="left")
        self.adPatWindow.createButton = tk.Button(self.adPatWindow.midFrame, text="Add Patient", command=self.adminPatCreate, background="#a7c194")
        self.adPatWindow.createButton.pack(side="left")
        self.adPatWindow.dischargeButton = tk.Button(self.adPatWindow.mid1Frame, background="#ed7990", text="Discharge Patient", command=self.patDischarge)
        self.adPatWindow.dischargeButton.pack(side="top")
        self.adPatWindow.dischargeAlert = tk.Label(self.adPatWindow.mid1Frame, background="#aab9e6", text=" ")
        self.adPatWindow.dischargeAlert.pack(side="top")
        self.adPatWindow.docLabel = tk.Label(self.adPatWindow.mid2Frame, text="Patient\'s Details", font=tkfont.Font(family='Helvetica', size=14, weight="bold"), background="#aab9e6")
        self.adPatWindow.docLabel.pack(side="top")
        #PATIENT DETAILS
        self.adPatWindow.patName = tk.Label(self.adPatWindow.botFrame, text="Select a patient", width=25, background="#a7a7a7")
        self.adPatWindow.patName.pack(side="top", expand="False")
        self.adPatWindow.patID = tk.Label(self.adPatWindow.botFrame, text=" ", width=25, background="#a7a7a7")
        self.adPatWindow.patID.pack(side="top", expand="False")
        self.adPatWindow.patAge = tk.Label(self.adPatWindow.botFrame, text=" ", width=25, background="#a7a7a7")
        self.adPatWindow.patAge.pack(side="top", expand="False")
        self.adPatWindow.patDoc = tk.Label(self.adPatWindow.botFrame, text=" ", width=25, background="#a7a7a7")
        self.adPatWindow.patDoc.pack(side="top", expand="False")
        self.adPatWindow.patNumb = tk.Label(self.adPatWindow.botFrame, text=" ", width=25, background="#a7a7a7")
        self.adPatWindow.patNumb.pack(side="top", expand="False")
        self.adPatWindow.patAddress = tk.Label(self.adPatWindow.botFrame, text=" ", width=35, background="#a7a7a7")
        self.adPatWindow.patAddress.pack(side="top", expand="False")
        self.adPatWindow.patSickness = tk.Label(self.adPatWindow.botFrame, text=" ", width=35, background="#a7a7a7")
        self.adPatWindow.patSickness.pack(side="top", expand="True")

    def patInfoDisp(self):
        for i in self.adPatWindow.patList.curselection():
            varA = f'{"Name:":>10} {patients[i].get_fullpName():>15}'
            varB = f'{"ID:":>10} {patients[i].get_pID():>15}'
            varC = f'{"Doctor:":>10} {patients[i].get_doc():>15}'
            varD = f'{"Number:":>10} {patients[i].get_numb():>15}'
            varE = f'{"Address:":>10} {patients[i].get_address():>25}'
            varF = f'{"Diagnosis:":>10} {str(patients[i].get_illess()):>15}'
            varG = f'{"Age:":>10} {str(patients[i].get_age()):>15}'
            self.adPatWindow.patName.config(text=varA)
            self.adPatWindow.patID.config(text=varB)
            self.adPatWindow.patDoc.config(text=varC)
            self.adPatWindow.patNumb.config(text=varD)
            self.adPatWindow.patAddress.config(text=varE)
            self.adPatWindow.patSickness.config(text=varF)
            self.adPatWindow.patAge.config(text=varG)
    
    def adminPatEdit(self):
        #Get patient
        for i in self.adPatWindow.patList.curselection():
            global selectedPat
            selectedPat = i
        global editingPat
        editingPat = copy.deepcopy(patients[selectedPat])
        #Window settings
        self.adPatEditWindow = tk.Toplevel()
        self.adPatEditWindow.title(editingPat.get_fullpName())
        self.adPatEditWindow.geometry("300x250")
        self.adPatEditWindow.resizable(0,0)
        self.adPatEditWindow.configure(bg="#aab9e6")
        #Frames
        self.adPatEditWindow.nameIDFrame = tk.Frame(self.adPatEditWindow, background="#aab9e6")
        self.adPatEditWindow.doctorFrame = tk.Frame(self.adPatEditWindow, background="#aab9e6")
        self.adPatEditWindow.IllnessFrame = tk.Frame(self.adPatEditWindow, background="#aab9e6")
        self.adPatEditWindow.EntryFrame = tk.Frame(self.adPatEditWindow, background="#aab9e6")
        self.adPatEditWindow.alertFrame = tk.Frame(self.adPatEditWindow, background="#aab9e6")
        self.adPatEditWindow.namebuttonFrame = tk.Frame(self.adPatEditWindow, background="#aab9e6")
        self.adPatEditWindow.buttonFrame = tk.Frame(self.adPatEditWindow, background="#aab9e6")
        self.adPatEditWindow.nameIDFrame.pack(side="top")
        self.adPatEditWindow.doctorFrame.pack(side="top")
        self.adPatEditWindow.IllnessFrame.pack(side="top")
        self.adPatEditWindow.EntryFrame.pack(side="top")
        self.adPatEditWindow.alertFrame.pack(side="top")
        self.adPatEditWindow.namebuttonFrame.pack(side="top")
        self.adPatEditWindow.buttonFrame.pack(side="top")
        #Content
        pnameID = f'{editingPat.get_fullpName():<15}|{editingPat.get_pID():^5}'
        self.adPatEditWindow.nameLab = tk.Label(self.adPatEditWindow.nameIDFrame, background="#aab9e6", text=pnameID, font=tkfont.Font(family='Helvetica', size=12, weight="bold"))
        self.adPatEditWindow.nameLab.pack(side="top")
        self.adPatEditWindow.doctorLab = tk.Label(self.adPatEditWindow.doctorFrame, background="#aab9e6", text=f'Doctor:  {editingPat.get_doc()}')
        self.adPatEditWindow.doctorLab.pack(side="top")
        self.adPatEditWindow.illnessLab = tk.Label(self.adPatEditWindow.IllnessFrame, background="#aab9e6", text=f'Diagnosis:  {editingPat.get_illess()}')
        self.adPatEditWindow.illnessLab.pack(side="top")
        self.adPatEditWindow.entry = tk.Entry(self.adPatEditWindow.EntryFrame, background="#a7b0c9")
        self.adPatEditWindow.entry.pack(side="top")
        self.adPatEditWindow.alertLabel = tk.Label(self.adPatEditWindow.alertFrame, background="#aab9e6", text=" ")
        self.adPatEditWindow.alertLabel.pack(side="top")
        #Buttons
        self.adPatEditWindow.nameButton = tk.Button(self.adPatEditWindow.namebuttonFrame, background="#a7b0c9", text="Set as First Name", command=self.patEditName1)
        self.adPatEditWindow.surnameButton = tk.Button(self.adPatEditWindow.namebuttonFrame, background="#a7b0c9", text="Set as Second Name", command=self.patEditName2)
        self.adPatEditWindow.ageButton = tk.Button(self.adPatEditWindow.buttonFrame, background="#a7b0c9", text="Set as Age", command=self.patEditAge)
        self.adPatEditWindow.numbButton = tk.Button(self.adPatEditWindow.buttonFrame, background="#a7b0c9", text="Set as Number", command=self.patEditNumb)
        self.adPatEditWindow.AddButton = tk.Button(self.adPatEditWindow.buttonFrame, background="#a7b0c9", text="Set as Address", command=self.patEditAdd)
        self.adPatEditWindow.nameButton.pack(side="left")
        self.adPatEditWindow.surnameButton.pack(side="left")
        self.adPatEditWindow.ageButton.pack(side="top")
        self.adPatEditWindow.numbButton.pack(side="top")
        self.adPatEditWindow.AddButton.pack(side="top")

    def patEditName1(self):
        editingPat.set_firstName(self.adPatEditWindow.entry.get())
        patients[selectedPat] = editingPat
        self.adPatEditWindow.alertLabel.config(text="First Name Changed")
    def patEditName2(self):
        editingPat.set_secondName(self.adPatEditWindow.entry.get())
        patients[selectedPat] = editingPat
        self.adPatEditWindow.alertLabel.config(text="Second Name Changed")
    def patEditAge(self):
        try:
            int(self.adPatEditWindow.entry.get())
        except:
            self.adPatEditWindow.alertLabel.config(text="Not a valid age")
        else:
            editingPat.set_age(self.adPatEditWindow.entry.get())
            patients[selectedPat] = editingPat
            self.adPatEditWindow.alertLabel.config(text="Age changed")
    def patEditNumb(self):
        editingPat.set_numb(self.adPatEditWindow.entry.get())
        patients[selectedPat] = editingPat
        self.adPatEditWindow.alertLabel.config(text="Number Changed")
    def patEditAdd(self):
        editingPat.set_address(self.adPatEditWindow.entry.get())
        patients[selectedPat] = editingPat
        self.adPatEditWindow.alertLabel.config(text="Address Changed")

    def adminPatCreate(self):
        #Window
        self.adPatCreateWindow = tk.Toplevel()
        self.adPatCreateWindow.title("Create Patient")
        self.adPatCreateWindow.geometry("300x150")
        self.adPatCreateWindow.resizable(0,0)
        self.adPatCreateWindow.configure(bg="#a7c194")
        #Frames
        self.adPatCreateWindow.nameFrame = tk.Frame(self.adPatCreateWindow, background="#a7c194")
        self.adPatCreateWindow.nameFrame.pack(side="top")
        self.adPatCreateWindow.surnameFrame = tk.Frame(self.adPatCreateWindow, background="#a7c194")
        self.adPatCreateWindow.surnameFrame.pack(side="top")
        self.adPatCreateWindow.ageFrame = tk.Frame(self.adPatCreateWindow, background="#a7c194")
        self.adPatCreateWindow.ageFrame.pack(side="top")
        self.adPatCreateWindow.buttonFrame = tk.Frame(self.adPatCreateWindow, background="#a7c194")
        self.adPatCreateWindow.buttonFrame.pack(side="top")
        #Inputs
        self.adPatCreateWindow.nameL = tk.Label(self.adPatCreateWindow.nameFrame, text="First name:")
        self.adPatCreateWindow.nameL.pack(side="left")
        self.adPatCreateWindow.nameE = tk.Entry(self.adPatCreateWindow.nameFrame, background="#d4d4d4")
        self.adPatCreateWindow.nameE.pack(side="left")
        self.adPatCreateWindow.surnameL = tk.Label(self.adPatCreateWindow.surnameFrame, text="Second name:")
        self.adPatCreateWindow.surnameL.pack(side="left")
        self.adPatCreateWindow.surnameE = tk.Entry(self.adPatCreateWindow.surnameFrame, background="#d4d4d4")
        self.adPatCreateWindow.surnameE.pack(side="left")
        self.adPatCreateWindow.ageL = tk.Label(self.adPatCreateWindow.ageFrame, text="Age:")
        self.adPatCreateWindow.ageL.pack(side="left")
        self.adPatCreateWindow.ageE = tk.Entry(self.adPatCreateWindow.ageFrame, background="#d4d4d4")
        self.adPatCreateWindow.ageE.pack(side="left")
        self.adPatCreateWindow.createButton = tk.Button(self.adPatCreateWindow.buttonFrame, text="Create Doctor", command=self.patientCreate, background="#d4d4d4")
        self.adPatCreateWindow.createButton.pack(side="top")
        self.adPatCreateWindow.warningText = tk.Label(self.adPatCreateWindow.buttonFrame, text=" ", background="#a7c194", font=tkfont.Font(family='Helvetica', size=14, weight="bold"))
        self.adPatCreateWindow.warningText.pack(side="top")

    def patientCreate(self):
        #Get Entered info
        enteredName = self.adPatCreateWindow.nameE.get().capitalize()
        enteredSname = self.adPatCreateWindow.surnameE.get().capitalize()
        enteredAge = self.adPatCreateWindow.ageE.get()
        patDupeCheck = False
        for i in range(len(patients)):
            if enteredName == patients[i].get_firstName() and enteredSname == patients[i].get_secondName():
                print("Name taken")
                patDupeCheck = True
                self.adPatCreateWindow.warningText.config(text="Name already taken")
                break
        if patDupeCheck == False:
            try:
                ageInt = int(enteredAge)
                newPat = Patient(enteredName, enteredSname, ageInt)
                patients.append(newPat)
            except ValueError:
                self.adPatCreateWindow.warningText.config(text="Invalid Age")
            except:
                print("Error creating doc")
            else:           #List update
                self.adPatWindow.patList.delete(0, len(patients))
                self.adPatCreateWindow.warningText.config(text="Patient Created")
                for i in range(len(patients)):
                    self.adPatWindow.patList.insert(i+1, f'{patients[i].get_fullpName()}  |  {patients[i].get_pID()}')

    def patDischarge(self):
        #Get patient
        for i in self.adPatWindow.patList.curselection():
            global selectedPat
            selectedPat = i
        global editingPat
        editingPat = copy.deepcopy(patients[selectedPat])
        if editingPat.get_doc() == "Unassigned":
            patients.pop(selectedPat)
            discharged_patients.append(editingPat)
            #List update
            self.adPatWindow.patList.delete(0, len(patients))
            self.adPatWindow.dischargeAlert.config(text="Patient removed")
            for i in range(len(patients)):
                self.adPatWindow.patList.insert(i+1, f'{patients[i].get_fullpName()}  |  {patients[i].get_pID()}')
        else:
            self.adPatWindow.dischargeAlert.config(text="Unassign patient from doctor to discharge")
            
    def adminDpatPage(self):
        #Window
        self.adDPatWindow = tk.Toplevel()
        self.adDPatWindow.title("Discharged Patients")
        self.adDPatWindow.geometry("400x350")
        self.adDPatWindow.resizable(0,0)
        self.adDPatWindow.configure(bg="#a2a2a2")
        #Frames
        self.adDPatWindow.topFrame = tk.Frame(self.adDPatWindow, background="#a2a2a2")
        self.adDPatWindow.topFrame.pack(side="top")
        self.adDPatWindow.midFrame = tk.Frame(self.adDPatWindow, background="#a2a2a2")
        self.adDPatWindow.midFrame.pack(side="top")
        self.adDPatWindow.botFrame = tk.Frame(self.adDPatWindow, background="#a2a2a2")
        self.adDPatWindow.botFrame.pack(side="top")
        #Content
        self.adDPatWindow.dpatList = tk.Listbox(self.adDPatWindow.topFrame, background="#828282", width=30)
        self.adDPatWindow.dpatList.pack(side="left")
        self.adDPatWindow.dpatList.grid(row=0, column=1, padx=5, pady=5)
        for i in range(len(discharged_patients)):           #List generation
            self.adDPatWindow.dpatList.insert(i+1, f'{discharged_patients[i].get_fullpName()}  |  {discharged_patients[i].get_pID()}')
        self.adDPatWindow.button = tk.Button(self.adDPatWindow.midFrame, text='Show info', command=self.dpatInfoDisp, background="#a2a2a2")
        self.adDPatWindow.button.pack(side="top")
        #Details
        self.adDPatWindow.patName = tk.Label(self.adDPatWindow.botFrame, text="Select a patient", width=25, background="#b1b1b1")
        self.adDPatWindow.patName.pack(side="top", expand="False")
        self.adDPatWindow.patID = tk.Label(self.adDPatWindow.botFrame, text=" ", width=25, background="#b1b1b1")
        self.adDPatWindow.patID.pack(side="top", expand="False")
        self.adDPatWindow.patAge = tk.Label(self.adDPatWindow.botFrame, text=" ", width=25, background="#b1b1b1")
        self.adDPatWindow.patAge.pack(side="top", expand="False")
        self.adDPatWindow.patNumb = tk.Label(self.adDPatWindow.botFrame, text=" ", width=25, background="#b1b1b1")
        self.adDPatWindow.patNumb.pack(side="top", expand="False")
        self.adDPatWindow.patAddress = tk.Label(self.adDPatWindow.botFrame, text=" ", width=25, background="#b1b1b1")
        self.adDPatWindow.patAddress.pack(side="top", expand="False")

    def dpatInfoDisp(self):
        for i in self.adDPatWindow.dpatList.curselection():
            varA = f'{"Name:":>10} {discharged_patients[i].get_fullpName():>15}'
            varB = f'{"ID:":>10} {discharged_patients[i].get_pID():>15}'
            varC = f'{"Number:":>10} {discharged_patients[i].get_numb():>15}'
            varD = f'{"Address:":>10} {discharged_patients[i].get_address():>25}'
            varE = f'{"Age:":>10} {str(discharged_patients[i].get_age()):>15}'
            self.adDPatWindow.patName.config(text=varA)
            self.adDPatWindow.patID.config(text=varB)
            self.adDPatWindow.patNumb.config(text=varC)
            self.adDPatWindow.patAddress.config(text=varD)
            self.adDPatWindow.patAge.config(text=varE)

#DOCTOR'S SECTION

    def docLogPage(self):
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
        self.docLogWindow.logButton = tk.Button(self.docLogWindow.botDocLogFrame, text="Log-in", bg="#1dd48e", command=self.docLogin)
        self.docLogWindow.logButton.pack(side="bottom")

    def docLogin(self):
        try:
            enteredID = self.docLogWindow.enterID.get()
            print("Login button was clicked")
            for i in range(len(doctors)):
                if enteredID.lower() == doctors[i].get_docID():
                    print("Login verified")
                    global loggedDoc
                    loggedDoc = i
                    self.doctorPage()
                    break
        except:
            print("Error logging in")

    def doctorPage(self):
        global loggedDoc
        self.docHomeWindow = tk.Toplevel()
        self.docHomeWindow.title("Doctor " + doctors[loggedDoc].get_fullName())
        self.docHomeWindow.geometry("350x250")
        self.docHomeWindow.resizable(0,0)
        self.docHomeWindow.configure(bg="#58f9bb")


    def patPage(self):
        print("WIP PATIENT")

def readPatients():
    with open("patients.csv", "r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            scannedPat = Patient(*row)
            patients.append(scannedPat)
        csvFile.close()

def writePatients():
    with open("patients2.csv", "w", newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(patients)

def main():
    readPatients()
    loginGUI()
    writePatients()

if __name__ == "__main__":
    main()
