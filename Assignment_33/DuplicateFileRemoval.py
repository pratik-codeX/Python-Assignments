import sys
import os
import email
import hashlib
import email_validator
import io
import time

def CheckSum(FileName):
    hobj = hashlib.md5()

    if os.path.isfile(FileName):
        fobj = open(FileName,"rb")
    else:
        print("Exception : [Errno 2] No such file or directory:"+ FileName+"Special Files")
        return                                                                                                                                                                                                                                  
    Buffer = fobj.read(io.DEFAULT_BUFFER_SIZE)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(io.DEFAULT_BUFFER_SIZE)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryPath):
    Duplicate = {}
    ret = os.path.exists(DirectoryPath)
    if ret == False:
        return "The Directory Does not Exists"
    
    ret = os.path.isdir(DirectoryPath)
    if ret == False:
        return "Invalid Folder"
    
    for Dir,Sub,File in os.walk(DirectoryPath):
        for fname in File:
            fname = os.path.join(Dir,fname)

            checksum = CheckSum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate
    
def DeleteDuplicate(DirectoryPath):

    start_time = time.perf_counter()    

    myDict = FindDuplicate(DirectoryPath)

    end_time = time.perf_counter()

    Total_time_Scanned = end_time - start_time

    print("Total Time for Directory Scanning : ",Total_time_Scanned)

    remove = lambda x :  len(x) > 1 

    result = list(filter(remove,myDict.values()))

    TotalFiles = 0
    DeleteFiles = 0
    for subresult in result:
        Flag = False
        for sub in subresult:
            if Flag == False:
                pass
            else:
                #os.remove(sub)
                pass
            DeleteFiles = DeleteFiles + 1
            Flag = True

    TotalFiles = TotalFiles + 1

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