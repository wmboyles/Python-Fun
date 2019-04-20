import smtplib  # mail server library

from os.path import basename
from os import remove

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

from zipFolder import zipFolder

'''
Sends an email from a given certain gmail address given a password.
Sender can be given any alias.
Email is sent to a given mail address with an optioal subject and message body.
Sender can optionally attach a list of file paths to be attached.
Sender can also attach an entire directory as a zipFile by specifying a directory name.
'''


def sendMail(alias, fromAddr, pw, toaddr, subject="", message="", AttchFileList=[], AttchFolderList=[]):
    msg = MIMEMultipart()  # create a message

    # setup the parameters of the message
    msg['From'] = alias + "<" + fromAddr + ">"  # FORMAT: "ALIAS <SEND ADDRESS>"
    msg['To'] = toaddr
    msg['Subject'] = subject
    
    # Add in the message body
    msg.attach(MIMEText(message, 'plain'))  # 'plain' or 'html'
    
    # add attachments as folders as a zip file
    for AttchFolder in AttchFolderList:
        zipFolder(AttchFolder)
        print("zipped " + AttchFolder)
        AttchFileList.append(AttchFolder + ".zip")

    # Attach Files from a list
    for AttchFile in AttchFileList:
        try:
            with open(AttchFile, "rb") as file:
                part = MIMEApplication(file.read(), Name=AttchFile)

            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(AttchFile)
            msg.attach(part)
            print("Attached " + AttchFile)
            
        except FileNotFoundError:
            if input(AttchFile + " not found. Send Anyways (Y/N)?").lower() != "y":
                print("Aborting Sending.")
                return

    # remove zip files that we just created and attached
    for AttchFolder in AttchFolderList:
        remove(AttchFolder + ".zip")

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()

    # Try to login to the mail service
    try:
        s.login(fromAddr, pw)  # do not turn on 2FA for this to work
    except smtplib.SMTPAuthenticationError:
        print("Invalid username or password. Aborting Sending.")
        return
    
    # send the message via the server just set up.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()

    print("Message Sent.")


if __name__ == '__main__':
    fromAlias = "FROM ALIAS"
    fromAddr = "FROM ADDRESS"
    fromPW = "FROM PASSWORD"
    toAddr = "TO ADDRESS"
    subject = "SUBJECT"
    message = "MESSAGE"
    fileList = [FILES]
    folderList = [FOLDERS]
    
    sendMail(fromAlias,  # From alias
             fromAddr,  # From address
             fromPW,  # Sender password
             toAddr,  # To address
             subject,  # Subject
             message,  # Message Body
             fileList,  # List of files to attach
             folderList  # Folder to attach
    )
