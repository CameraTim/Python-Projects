#Importing webbrowser module for internet browser access and tkinter module for GUI
import webbrowser
import tkinter
from tkinter import *

#Initializing the tkinter GUI window
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        frameW = 500
        frameH = 125
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(frameW,frameH))
        self.master.title('Webpage Text Input')
        self.master.config(bg='lightgray')
        #This function calculates the user's screen height and width to determine the center of the screen
        centerWindow(self,frameW,frameH)

        #Creating the label for the entry box
        self.lbl_html = Label(self.master, text='Website Text Entry:', bg="lightgray")
        self.lbl_html.grid(row=0, column=0, padx=(20,0), pady=(10,0), sticky=N+S+W)

        #Creating the Entry box where the user adds their keyboard input
        self.txt_user = Entry(self.master, width=75)
        self.txt_user.grid(row=1, column=0, padx=(20,0), pady=(5,0))

        #Connecting a buttom to the html function
        self.btn_submit = Button(self.master,text='Submit', fg='black', width=10, command=self.htmlText)
        self.btn_submit.grid(row=2, column=0, padx=(50,0), pady=(20,0), sticky=N+S+W)

    #This function pulls the string from the text box and inserts it into the HTML code file with the .format wildcard
    def htmlText(self):
        userEntry = self.txt_user.get()
        #opening the file and overwriting it (will create a new file if it doesn't exist)
        file = open("header.html", "w")
        file.write("""
        <html>
            <body>
                <h1>
                {}
                </h1>
            </body>
        </html>
        """.format(userEntry))
        file.close()
        #Opens a new browser tab or window if one isn't already opened
        webbrowser.open_new("header.html")

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
