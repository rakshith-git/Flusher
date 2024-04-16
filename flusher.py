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
fileTypeLists = {
    dst_folder_pdfs: ["*.pdf", "*.docx", "*.xlsx", "*.pptx"],
    dst_folder_images: ["*.jpg", "*.png", "*.jpeg"],
}


def moveFiles(fileType, destination):
    for file in fileType:
        file_name = os.path.basename(file)
        shutil.move(file, os.path.join(destination, file_name))
        print("Moved:", file)


def assignAndMoveFiles(destination, fileTypeList):
    for fileType in fileTypeList:
        typeList = []
        typeList.append(glob.glob(os.path.join(directory, fileType)))
        for type in typeList:
            moveFiles(type, destination)


for key, value in fileTypeLists.items():
    assignAndMoveFiles(key, value)


def updateDesktopList():
    desktopList.clear()
    files_and_dirs = os.listdir(directory)
    for item in files_and_dirs:
        desktopList.append(item)
