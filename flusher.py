import os
import shutil
import glob

directory = "C:/Users/win10/Desktop"
dst_folder_pdfs = "C:/Users/win10/Desktop/pdfs"
dst_folder_images = "C:/Users/win10/Desktop/images"
desktopList = []
files_and_dirs = os.listdir(directory)

fileTypeListForDocs = ["*.pdf", "*.docx", "*.xlsx", "*.pptx"]
fileTypeListForImages = ["*.jpg", "*.png", "*.jpeg"]


def moveFiles(fileType, destination):
    for file in fileType:
        file_name = os.path.basename(file)
        shutil.move(file, os.path.join(destination, file_name))
        print("Moved:", file)


for fileType in fileTypeListForDocs:
    typeList = []
    typeList.append(glob.glob(os.path.join(directory, fileType)))
    for type in typeList:
        moveFiles(type, dst_folder_pdfs)

for fileType in fileTypeListForImages:
    typeList = []
    typeList.append(glob.glob(os.path.join(directory, fileType)))
    for type in typeList:
        moveFiles(type, dst_folder_images)


def updateDesktopList():
    desktopList.clear()
    files_and_dirs = os.listdir(directory)
    for item in files_and_dirs:
        desktopList.append(item)
