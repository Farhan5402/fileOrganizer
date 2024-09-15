import os
from datetime import date
import shutil

docs = (".pdf",".docx",".xlsx",".doc",".pages")

media = (".mp3",".mp4",".avi",".jpg",".jpeg")

applications = (".dmg")

def check_create_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)

if __name__ == '__main__':

    downloadPath = "/Users/farhan121/Downloads"
    today = date.today()
    dateString = today.strftime("%B %d, %Y")
    organizedPath = downloadPath + '/FileOrganizer-' + dateString
    countFile = 0
    countFolder = 0

    check_create_folder(organizedPath)

    os.chdir(downloadPath)

    for file in os.listdir():
        extension = os.path.splitext(file)[1]
        # print(os.path.isdir(file))

        if file == ".DS_Store":
            continue

        if "FileOrganizer" in file:
            continue

        countFile+=1

        if not extension:
            countFile-=1
            countFolder+=1
            check_create_folder(organizedPath + '/Folders')
            shutil.move(file, organizedPath + '/Folders')
        elif extension in docs:
            check_create_folder(organizedPath+'/Documents')
            shutil.move(file, organizedPath+'/Documents')
        elif extension in media:
            check_create_folder(organizedPath + '/Media')
            shutil.move(file, organizedPath+'/Media')
        elif extension in applications:
            check_create_folder(organizedPath + '/Apps')
            shutil.move(file, organizedPath+'/Apps')
        else:
            check_create_folder(organizedPath + '/Others')
            shutil.move(file, organizedPath + '/Others')

    print(f"{countFolder} folders and {countFile} files have been organized")
