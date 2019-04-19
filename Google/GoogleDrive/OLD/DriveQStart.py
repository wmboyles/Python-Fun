from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#Gets list of files in root (main menu) of drive 
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

#Gets first file's (most recently created) ID
fid1 = '%s'%((file_list[0])['id'])
print(fid1+'\n') #Folder ID

'''
#Creates a folder (Currently called TESTING2) inside the previouslylocated folder
folder_metadata = {
    'title': 'TESTING2',
    'mimeType': 'application/vnd.google-apps.folder',
    'parents': [{'kind': 'drive#fileLink', 'id': fid1}]
    }

folder = drive.CreateFile(folder_metadata)
folder.Upload()

#Stores this subfolder's id
fid2 = '%s'%(folder['id'])
print(fid2)
'''

#Creates and uploads a file into this subfolder
file_metadata = {
    'parents': [{'kind':'drive#fileLink', 'id':fid1}]
    }
file = drive.CreateFile(file_metadata)
file.SetContentFile('C:\\Users\\willi\\Desktop\\CI_Folder')
file.Upload()
