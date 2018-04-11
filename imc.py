#-------------------------------------------------------------------------------
# Name:       imc.py
# Purpose: imc(Image Metadata Collector).
#The program will collect image metadata.
#Versioning and progress will be managaed through GitHub
#
# Author:      halla, WEGC
#
# Created:     04/04/2018

def main():
    pass

if __name__ == '__main__':
    main()

#Imports regular expressions. Is used to validate file name
import re

#import GUI library
from tkinter import *

#for Python V3 you must explicitely load the messagebox
import tkinter.messagebox

class ImageMD:
    #Image Metadata
    def __init__(self, imageID, fileName, fileExtension, imageName, owner, licence, photoCategory):
        self.imageID= imageID
        self.fileName= fileName
        self.fileExten= fileExtension
        self.name= imageName
        self.owner= owner
        self.licence= licence
        self.photoC= photoCategory

    def get_imageID(self):
        return self.imageID

    def get_fileName(self):
        return self.fileName

    def get_fileExten(self):
        return self.fileExten

    def get_name(self):
        return self.name

    def get_owner(self):
        return self.owner

    def get_licence(self):
        return self.licence

    def get_photoC(self):
        return self.photoT

class GUI:
    #default colour variables makes changing colours easier
    global bkcolour
    global maintxtcolour
    global mainfont
    bkcolour= '#c0deed'
    maintxtcolour= 'black'
    mainfont = ('Times', '24')

    def __init__(self):

        window = Tk()
        window.title("Data Entry for Image Metadata")
        window.minsize(width = 400, height= 600)
       # window.configure(bg= bkcolour)

        heading_label = Label(window, bg = bkcolour, fg = maintxtcolour, text= "TITLE HERE", font= mainfont)
        heading_label.pack()

        #INITIALIZATION VARIABLES
        #this variable stores whether the data has been validated or not
        self.ready_to_write = False
        #this will contain the list of all schools entered via the gui
        self.recordlist = []

        
        #creating label and field variable in GUI for each entry field
        fileName_label = Label(window, text='Please enter the filename:')
        fileName_label.grid(row = 0 , column = 0 #.pack() places the component in the window
        self.fileName_field = Entry(window)
        self.fileName_field.pack(anchor = 'c')

        #code for dropdown menu
        FileExten_label = Label(window, text='Select File Extension')
        FileExten_label.pack(anchor = 'c')
        self.fileExten_field = StringVar()
        OptionMenu(window, self.fileExten_field, ".jpg", ".png", ".jpeg", ".gif").pack(anchor = 'c') #Most common image file types

        imageID_label = Label(window, text='Enter image ID number:')
        imageID_label.pack()
        self.imageID_field = Entry(window)
        self.imageID_field.pack()
        
        name_label = Label(window, text='Enter image Name:')
        name_label.pack()
        self.name_field = Entry(window)
        self.name_field.pack()

        owner_label = Label(window, text="Enter Owner's Name:")
        owner_label.pack()
        self.owner_field = Entry(window)
        self.owner_field.pack()
        ##self.owner_field.set("WEGC") #Assumes most images with be owned by overseeing organisation

        Licence_label = Label(window, text='Select image licence')
        Licence_label.pack(anchor = 'c')
        self.licence_field = StringVar()
        OptionMenu(window, self.licence_field, "1", "2", "3", "4", "5", "6").pack(anchor = 'c') #Must add correct Image licence types

        PhotoC_label = Label(window, text='Select photo category')
        PhotoC_label.pack(anchor = 'c')
        self.photoC_field = StringVar()
        OptionMenu(window, self.photoC_field, "Landscape", "Person", "Group", "Document", "Signage", "Object", "Other").pack(anchor = 'c')


        #creates a button. The command function is run when the button is pressed
        #the 'command=self.doSubmit' is an example of a callback method
        button_label = Label(window, text='Press to validate:')
        button = Button(window, text='Submit', command=self.doSubmit)

        button_label1 = Label(window, text='Convert Record to csv')
        button1 = Button(window, text='Write To CSV', command=self.writetocsv)
        button_label.pack(anchor = 'c')
        button.pack(anchor = 'c')
        button_label1.pack(anchor = 'c')
        button1.pack(anchor = 'c')

        #Waits for an event
        window.mainloop()

    def doSubmit(self):

    #test uniqueness of each school name entered u
        noduplicate = True;
        for record in self.recordlist:
            if self.fileName.get() == record.fileName():
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate file name');
                print('Please enter file name again');


        if noduplicate == True:
        #this is the callback method for the 'Submit' button
            if len(self.imageID_field.get()) <1 or len(self.fileName_field.get()) <1 or len(self.fileExten_field.get()) <1 or len(self.owner_field.get()) <1 or len(self.name_field.get()) <1 or len(self.licence_field.get()) <1 or len(self.photoC_field.get()) <1:
                tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')
            elif self.imageID.get() != int: 
                tkinter.messagebox.showwarning('Warning!','Please enter a numerical value for image ID.')
            elif self.imageID.get() == record.imageID :
                 tkinter.messagebox.showwarning('Warning!','Please enter a different numerical value for image ID, this one already exists.')
            else:
                    if re.match("^[a-zA-Z0-9_]+$", self.fileName_field.get()): #Checking that there is only letters, numbers, and undersocores
                        print("Only alphabetical letters and spaces: yes") #For testing purposes


                        #beause all imformation entered has been checking and is good.
                        self.recordlist.append(ImageMD(self.imageID_field.get(),self.fileName_field.get(),self.fileExten_field.get(), self.owner_field.get() , self.name_field.get(), self.licence_field.get(), self.photoC_field.get() ))
                        self.ready_to_write= True
                        tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                        self.fileName_field.delete(0, END) #command to clear field
                        self.num_classrooms_field.delete(0, END)

                    else:
                        print("Please only use letters of the alphabet or numbers for file name. No special characters except undersorces.")

    def writetocsv(self):
        #This what happens upon clicking the "Write to CSV" button
        import csv
        file_name = 'test1.csv' #I prefer csv files are automativally opened by excel rather than notepad

        if self.ready_to_write: #Connects to function that checks data has been validated

            ofile = open(file_name, 'w') #Open file with overwriting permissions.
            writer = csv.writer(ofile, delimiter =",", lineterminator = "\n")
            for record in self.recordlist:
                print(record.full_file_name())
                writer.writerow([record.get_imageID(), record.get_fileName, record.get_fileExtension(), record.get_imageName(), record.get_owner(), record.get_licence(), record.get_photoC()])

            ofile.close()#To Explicitly close file
            tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

        self.ready_to_write= False #Resetting variables

#Initialises the programme
GUI()
