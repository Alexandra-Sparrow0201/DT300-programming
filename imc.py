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
