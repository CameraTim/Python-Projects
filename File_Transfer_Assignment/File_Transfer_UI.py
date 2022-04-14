import tkinter
from tkinter import *
from tkinter import filedialog as fi
from tkinter import messagebox
import shutil
import os
from datetime import datetime

#Initializing the tkinter GUI window
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        frameW = 565
        frameH = 175
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(frameW,frameH))
        self.master.title('File Transfer')
        self.master.config(bg='lightgray')
        #This function calculates the user's screen height and width to determine the center of the screen
        centerWindow(self,frameW,frameH)

        #Creating the label, button, and entry layout
        self.lblBrowse1 = Label(self.master, text='Source Folder:', bg="lightgray")
        self.lblBrowse1.grid(row=0, column=0, padx=(25,0), pady=(10,0), sticky=N+S+W)

        self.lblBrowse2 = Label(self.master, text='Destination Folder:', bg="lightgray")
        self.lblBrowse2.grid(row=0, column=2, padx=(25,0), pady=(10,0), sticky=N+S+W)

        self.btnBrowse1 = Button(self.master,text='Browse', fg='black', width=12, command=self.openSource)
        self.btnBrowse1.grid(row=1, column=0, padx=(25,0), pady=(10,0), sticky=N+S+W)

        self.btnBrowse2 = Button(self.master,text='Browse', fg='black', width=12, command=self.openDest)
        self.btnBrowse2.grid(row=1, column=2, padx=(25,0), pady=(10,0), sticky=N+S+W)

        self.txtBrowse1 = Entry(self.master, fg="black", width=40)
        self.txtBrowse1.grid(row=2, column=0, padx=(25,0), pady=(15,0))

        self.txtBrowse2 = Entry(self.master, fg="black", width=40)
        self.txtBrowse2.grid(row=2, column=2, padx=(25,0), pady=(15,0))

        self.btnSubmit = Button(self.master,text='Move Old Files', fg='black', width=15, command=self.subFile)
        self.btnSubmit.grid(row=3, column=0, padx=(25,0), pady=(25,0), sticky=N+S+W)

    #Function for selecting the source folder
    def openSource(self):
        sourceInput = fi.askdirectory()
        self.txtBrowse1.insert(0,sourceInput)
    #Function for selecting the destination folder
    def openDest(self):
        destInput = fi.askdirectory()
        self.txtBrowse2.insert(0,destInput)

    #Runs a time and folder check for moving files
    def subFile(self):
        #Pulls current time and converts to Unix time
        hourPoint = datetime.now()
        unixHour = datetime.timestamp(hourPoint)

        #Pulling the folders from the Entry boxes
        source = self.txtBrowse1.get()
        dest = self.txtBrowse2.get()
        #Check to see if the Entry boxes are empty
        if source == '' or dest == '':
            messagebox.showerror("Missing Info","Please enter a source and destination folder.")
        else:
            #Each folder requires a / at the end to concatinate the file properly
            source = source + "/"
            dest = dest + "/"
            try:
                #Pulls both the source and destination folders to see if they exist
                files = os.listdir(source)
                destCheck = os.listdir(dest)
                for i in files:
                    #Pulling the modified time of the files and running a check to see if the files were modified
                    #within the past 24 hours
                    x = os.path.getmtime(source + '{}'.format(i))
                    y = abs(x - unixHour)
                    if y >= 86400:
                        shutil.move(source+i, dest)
                messagebox.showinfo("Success!","File transfer complete!")
            #Skips running the file move if the directory does not exist
            except FileNotFoundError:
                messagebox.showerror("Wrong Directory","Folder not found, please try a different folder path.")
            
                        
#Calculating the center point of the current active monitor to center the GUI
def centerWindow(self, w, h):
    screenW = self.master.winfo_screenwidth()
    screenH = self.master.winfo_screenheight()
    x = int((screenW/2) - (w/2))
    y = int((screenH/2) - (h/2))
    centerSpot = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerSpot

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
