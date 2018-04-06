#-------------------------------------------------------------------------------
# Name:       imc.py
# Purpose: imc(Image Metadata Collector).
#The program will collect image metadata.
#Versioning and progress will be managaed through GitHub
#
# Author:      halla, WEGC
#
# Created:     04/04/2018

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

        heading_label = Label(window, bg = bkcolour, fg = maintxtcolour, text= "TITLE HERE", font= mainfont)
        heading_label.pack()

        #creating label and field variable in GUI for each entry field
        fileName_label = Label(window, text='Please enter the filename:')
        fileName_label.pack(anchor="c") #.pack() places the component in the window
        self.fileName_field = Entry(window)
        self.fileName_field.pack(anchor="c")

        #code for dropdown menu
        fileExten_label = Label(window, text='Select File Extension')
        fileExten_label.pack()
        self.fileExten_field = StringVar()
        OptionMenu(window, self.fileExten_field, ".jpg", ".png", ".jpeg", ".gif").pack() #Most common image file types

        name_label = Label(window, text='Enter image Name:')
        name_label.pack(anchor="c")
        self.name_field = Entry(window)
        self.name_field.pack(anchor="c")

        owner_label = Label(window, text="Enter Owner's Name:")
        owner_label.pack(anchor="c")
        self.owner_field = Entry(window)
        self.owner_field.pack(anchor="c")

        licence_label = Label(window, text='Select image licence')
        licence_label.pack()
        self.licence_field = StringVar()
        OptionMenu(window, self.licence_field, "1", "2", "3", "4", "5", "6").pack()

        fileExten_label = Label(window, text='Select photo category')
        fileExten_label.pack()
        self.fileExten_field = StringVar()
        OptionMenu(window, self.fileExten_field, "landscape", "person", "group", "document", "signage", "object").pack()

        #Waits for an event
        window.mainloop()


#Initialises the programme
GUI()