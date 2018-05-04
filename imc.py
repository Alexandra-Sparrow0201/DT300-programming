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

#Importing CSV library
import csv

#import GUI library
from tkinter import *

#explicitely loads the messagebox
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
        return self.photoC
    
    def full_file_name(self):
        file = self.fileName + self.fileExten
        return file

class GUI:
    #default colour variables makes changing colours easier
    global bkcolour
    global maintxtcolour
    global tfont
    global mainfont
    global bcolour
    bkcolour= '#c0deed' #Background colour
    bcolour = '#4885ed' #For buttons 
    maintxtcolour= 'black'
    tfont = ('Calibri', '12')# For the text
    mainfont = ('Calibri', '24') #For the header

    def __init__(self):

        window = Tk()
        window.title("Data Entry for Image Metadata")
        window.minsize(width = 370, height= 400) #Widget size determined through trial and error
        window.configure(bg = bkcolour)

        heading_label = Label(window, fg = maintxtcolour,bg = bkcolour, text= "Image Metadata", font= mainfont)
        heading_label.grid(row = 0, columnspan = 2, sticky = W+E)
        

        #INITIALIZATION VARIABLES
        #this variable stores whether the data has been validated or not
        self.ready_to_write = False
        #this will contain the list of all image metadata entered via the gui
        self.recordlist = []

        
        #creating label and field variable in for each entry field
        fileName_label = Label(window, text='Please enter the filename:',bg = bkcolour, font= tfont)
        fileName_label.grid(row = 1 , column = 0, padx =5, pady =2 ) #.grid places the component in the window in a grid format
        self.fileName_field = Entry(window)
        self.fileName_field.grid(row = 2, column = 0, padx =5, pady =5)
        self.fileName_field.focus()

        #code for dropdown menu
        FileExten_label = Label(window, text='Select file extension',bg = bkcolour, font= tfont)
        FileExten_label.grid(row = 1, column = 1, padx =5, pady =2)
        self.fileExten_field = StringVar()
        OptionMenu(window, self.fileExten_field, ".jpg", ".png", ".jpeg", ".gif").grid(row = 2, column = 1, padx =5, pady =5 ) #Most common image file types
        #This is not cleared as if you are entering multiple images this is unlikely to change often
        
        imageID_label = Label(window, text='Enter image ID number:',bg = bkcolour, font= tfont)
        imageID_label.grid(row = 3, column = 0, sticky = W , padx =5, pady =5)
        self.imageID_field = Entry(window)
        self.imageID_field.grid(row = 3, column = 1, padx =5, pady =5 )
        
        name_label = Label(window, text='Enter image name:', bg = bkcolour, font= tfont)
        name_label.grid(row = 4, column = 0, sticky = W, padx =5, pady =5 )
        self.name_field = Entry(window)
        self.name_field.grid(row = 4, column = 1)

        owner_label = Label(window, text="Enter Owner's name:",bg = bkcolour, font= tfont)
        owner_label.grid(row = 5, column = 0, sticky = W, padx =5, pady =5 )
        self.owner_field = Entry(window)
        self.owner_field.grid(row = 5, column = 1, padx =5, pady =5 )
        self.owner_field.insert(END, 'WEGC') #Assumes most images with be owned by overseeing organisation

        Licence_label = Label(window, text='Select image licence acronym',bg = bkcolour, font= tfont)
        Licence_label.grid(row = 6, column = 0, padx =5, pady =5 )
        self.licence_field = StringVar()
        OptionMenu(window, self.licence_field, "CC0", "BY", "BY-SA", "BY-NC", "BY-ND", "BY-NC-SA", "BY-NC-ND").grid(row = 7, column = 0, padx =5, pady =5 ) #Must add correct Image licence types
        #This is not cleared as if you are entering multiple images this is unlikely to change often
        
        PhotoC_label = Label(window, text='Select photo category',bg = bkcolour, font= tfont)
        PhotoC_label.grid(row = 6, column = 1, padx =5, pady =5 )
        self.photoC_field = StringVar()
        OptionMenu(window, self.photoC_field, "Landscape", "Person", "Group", "Document", "Signage", "Object", "Other").grid(row = 7, column = 1, padx =5, pady =5 )
        #This is not cleared as if you are entering multiple images this is unlikely to change often

        #creates a button. The command function is run when the button is pressed
        #the 'command=self.doSubmit' is an example of a callback method
        #button_label = Label(window, text='Press to validate:',bg = bkcolour, font= tfont) Not needed
        button = Button(window,bg = bcolour, text='Validate and Submit', command=self.doSubmit)

        #button1_label = Label(window, text='Convert record to csv',bg = bkcolour, font= tfont) Not needed
        button1 = Button(window, bg = bcolour, text='Write to csv', command=self.writetocsv)
        
        #button_label.grid(row = 8, column = 0, padx =5, pady =5 )
        button.grid(row = 8, column = 0, padx =5, pady =5 )
        #button1_label.grid(row = 8, column = 1, padx =5, pady =5 )
        button1.grid(row = 8, column = 1, padx =5, pady =5 )

        #Waits for an event
        window.mainloop()

    def doSubmit(self):
        #This runs when the submit button is pressed
        noduplicate = True;
        #test uniqueness of each file name entered
        for record in self.recordlist:
            if self.fileName_field.get() == record.get_fileName():
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate file name');
                print('Please enter file name again');
                
        #Test uniqueness of each image ID entered            
        for record in self.recordlist:
            if self.imageID_field.get() == record.get_imageID():
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Please enter a different numerical value for image ID, this one already exists.')
                print('Please enter image ID again');


        if noduplicate == True:
            if len(self.fileName_field.get()) > 250: 
                tkinter.messagebox.showwarning('Warning!','File Name has exceeded maximum character length of 250 please reduce input.')
                
            elif len(self.imageID_field.get()) <1 or len(self.fileName_field.get()) <1 or len(self.fileExten_field.get()) <1 or len(self.owner_field.get()) <1 or len(self.name_field.get()) <1 or len(self.licence_field.get()) <1 or len(self.photoC_field.get()) <1:
                tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')
                
            else:
                try:
                    validated_imageID = int(self.imageID_field.get())
                    if validated_imageID <= 0:
                       tkinter.messagebox.showwarning("Error", "Make sure image ID is greater than zero")
                       ready_to_write = False
                       
                    elif validated_imageID >250:
                        tkinter.messagebox.showwarning("Error", "Make sure image ID is less than 250")
                        ready_to_write = False
                    
                    elif re.match("^[a-zA-Z0-9_]+$", self.fileName_field.get()): #Checking that there is only letters, numbers, and underscores
                        #print("Only alphabetical letters and spaces: yes") #For testing purposes

                        #beause all imformation entered has been checking and is good.
                        self.recordlist.append(ImageMD(self.imageID_field.get(),self.fileName_field.get(),self.fileExten_field.get(), self.owner_field.get() , self.name_field.get(), self.licence_field.get(), self.photoC_field.get() ))
                        self.ready_to_write= True
                        tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                        self.fileName_field.delete(0, END) #command to clear fields
                        self.imageID_field.delete(0, END)
                        self.name_field.delete(0, END)
                        self.fileName_field.focus()#Moves cursor to file name field
                    else:
                        tkinter.messagebox.showwarning("Error", "Please only use letters of the alphabet or numbers for file name. No special characters except undersorces.")

                except:
                    tkinter.messagebox.showwarning('Warning!','Please enter numeric image ID.')
                    print('Please enter image ID')
                    
                
                

    def writetocsv(self):
        #This what happens upon clicking the "Write to CSV" button
        """for record in self.recordlist: #For testing purposes
                print(record.full_file_name())"""
        
        file_name = 'image_meta.csv' #I prefer csv files are automativally opened by excel rather than notepad

        if self.ready_to_write: #Checks data has been validated

            ofile = open(file_name, 'w') #Open file with overwriting permissions. I use the the w because it means I dont have to the clear the list each time and therefore will not be able to check against other entries for dupilicates.
            writer = csv.writer(ofile, delimiter =",", lineterminator = "\n")
            for record in self.recordlist:
                print(record.full_file_name())
                writer.writerow([record.get_imageID(), record.get_fileName(), record.get_fileExten(), record.get_name(), record.get_owner(), record.get_licence(), record.get_photoC()])
                tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')
            ofile.close()#To Explicitly close file
            
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

        self.ready_to_write= False #Resetting variables

#Initialises the programme
GUI()
