import sys
import os
import email
import email_validator

def DirectoryTraversal(DirectoryPath):
    ret = os.path.exists(DirectoryPath)
    if ret == False:
        print("The Directory Does not Exists")
        return
    ret = os.path.isdir(DirectoryPath)
    if ret == False:
        print("Invalid Folder")
        return
    
    for Dir,Sub,File in os.walk(DirectoryPath):
        for fname in File:

            pass

def DeleteDuplicate(DirectoryPath):
    


def main():
    Boarder = "-"*50
  
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print(Boarder)
            print(f"Duplicate File Removal Automation\n")
            print(f'''This script scans a directory, identifies duplicate files using
checksums, deletes duplicate files, creates a log file,
and sends the log file through email.''')
        elif(sys.argv[1] == "-u" or sys.argv[1] == "--Usage"):
            print(f''' 
                    python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>
                    Example:
                            python DuplicateFileRemoval.py E:/Data/Demo 50
                            marvellousinfosystem@gmail.com
                    ''')
        else:
            print(f'''Enter the Source Code as :
pythonfile.py -h or -u for more information.''')

    elif(len(sys.argv) == 4):
        DirectoryName = sys.argv[1]
        ret = os.path.exists(DirectoryName)
        if ret == False:
            print("Error : The Directory Does not Exists")
            return
        ret = os.path.isdir(DirectoryName)
        if ret == False:
            print("Error : Invalid Folder")
            return

        Interval = sys.argv[2]

        if int(Interval) <= 0 :
            print("Error : Invalid Interval of Time it must be positive")
            return
        
        ReceiverEmail = sys.argv[3]
        try:
            ret = email_validator.validate_email(ReceiverEmail)
        except Exception as eobj:    
            print("Error : Invalid email",eobj)

        DeleteDuplicate(DirectoryName)

    else:
        print(f'''Enter the Source Code as :
                pythonfile.py -h or -u for more information.''')

  

if __name__ == "__main__":
    main()