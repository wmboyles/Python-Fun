from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import listdir

# SETUP
gauth = GoogleAuth()
#gauth.LocalWebserverAuth()
gauth.CommandLineAuth()
gauth.LoadCredentialsFile("mycreds.txt")



#Makes sure you can upload w/o having to login every time
if gauth.credentials is None: gauth.LocalWebserverAuth()
elif gauth.access_token_expired: gauth.Refesh()
else: gauth.Authorize()



gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)


#Lists all non-trashed files in drive folder
#Use 'root' if no parent id
def listContents(parentID):
    query = ("'%s' in parents and trashed=false"%(parentID))
    file_list = drive.ListFile({'q': query}).GetList()
    for file in file_list:
        print("Name: {}".format(file['title']))
        print("ID: {}\n".format(file['id']))


#Makes and uploads an empty folder
def makeFolder(parentID, driveFolderName):
    folder_metadata = {
        'title': driveFolderName,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [{'kind': 'drive#fileLink', 'id': parentID}]
    }
    folder = drive.CreateFile(folder_metadata)
    print("Uploading {0} to {1}".format(driveFolderName,parentID))
    folder.Upload()
    return '%s'%(folder['id']) #Returns folder id


#Makes and uploads a folder filled with content from computer
#Use 'root' as parentID if you want to upload a folder to the main menu
#Make sure the localFolderPath uses '\\' -- ex 'C:\\users\\bob\\Desktop\\folder1'
#Local path can be from C: or directory of program
def uploadFolder(parentID,localFolderPath,driveFolderName):
    fid = makeFolder(parentID,driveFolderName)
    for filename in listdir(localFolderPath):
        file_metadata = {
            'title': filename,
            'parents': [{'kind':'drive#fileLink', 'id':fid}]
        }
        file = drive.CreateFile(file_metadata)
        file.SetContentFile(localFolderPath+'\\'+filename)
        print("Uploading {0} to {1}".format(filename,driveFolderName))
        file.Upload()


#Uploads a single document to a folder
#Make sure the localPath uses '\\' -- ex 'C:\\users\\bob\\Desktop\\beach.jpg'
#Local path can be from C: or directory of program
def uploadDoc(parentID,localPath,driveName):
    file_metadata = {
        'title': driveName,
        'parents': [{'kind': 'drive#fileLink', 'id':parentID}]
    }
    file = drive.CreateFile(file_metadata)
    file.SetContentFile(localPath)
    print("Uploading {0} as {1} to {2}".format(localPath,driveName,parentID))
    file.Upload()


##########################################################################################


def main():
    uploadFolder('','','')

main()
