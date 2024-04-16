import os
import shutil
import glob

# set the Desktop path here
directory = "C:/Users/win10/Desktop"


# set the documents path here
dst_folder_pdfs = "C:/Users/win10/Desktop/pdfs"
# set the images path here
dst_folder_images = "C:/Users/win10/Desktop/images"

desktopList = []
files_and_dirs = os.listdir(directory)

# you can change the file types here
fileTypeListForDocs = ["*.pdf", "*.docx", "*.xlsx", "*.pptx"]
fileTypeListForImages = ["*.jpg", "*.png", "*.jpeg"]


def moveFiles(fileType, destination):
    for file in fileType:
        file_name = os.path.basename(file)
        shutil.move(file, os.path.join(destination, file_name))
        print("Moved:", file)


def assignAndMoveFiles(fileTypeList, destination):
    for fileType in fileTypeList:
        typeList = []
        typeList.append(glob.glob(os.path.join(directory, fileType)))
        for type in typeList:
            moveFiles(type, destination)


assignAndMoveFiles(fileTypeListForDocs, dst_folder_pdfs)
assignAndMoveFiles(fileTypeListForImages, dst_folder_images)


def updateDesktopList():
    desktopList.clear()
    files_and_dirs = os.listdir(directory)
    for item in files_and_dirs:
        desktopList.append(item)
