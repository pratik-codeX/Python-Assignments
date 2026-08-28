import sys
import os
import email
import hashlib
import email_validator
import io
import time
from LogFile import Log
import datetime

class DeleteDuplicate:
    def __init__(self,DirectoryPath,Email):
        self.DirectoryPath = DirectoryPath
        self.Email = Email
        #self.FileLog = Log

    def CheckSum(self,FileName):
        hobj = hashlib.md5()

        if os.path.isfile(FileName):
            fobj = open(FileName,"rb")
        else:
            File = open(self.FileLog,"w")
            File.write()
            print("Exception : [Errno 2] No such file or directory:"+ FileName+"Special Files")
            return                                                                                                                                                                                                                                  
        Buffer = fobj.read(io.DEFAULT_BUFFER_SIZE)

        while(len(Buffer) > 0):
            hobj.update(Buffer)
            Buffer = fobj.read(io.DEFAULT_BUFFER_SIZE)

        fobj.close()

        return hobj.hexdigest()

    def FindDuplicate(self):
        File = Log()
        Cnt = 0
        Duplicate = {}
        ret = os.path.exists(self.DirectoryPath)
        if ret == False:
            File.write("Error : The Directory Does not Exists\n")
            return "The Directory Does not Exists"
        
        ret = os.path.isdir(self.DirectoryPath)
        if ret == False:
            File.write("Error : Invalid Folder")
            return "Invalid Folder"
        
        for Dir,Sub,File1 in os.walk(self.DirectoryPath):
            for fname in File1:
                Cnt = Cnt + 1
                File.write(f"Total Files Scanned are :{Cnt}\n")
                fname = os.path.join(Dir,fname)

                checksum = self.CheckSum(fname)
                Cnt1 = 0

                if checksum in Duplicate:
                    Cnt1 = Cnt1 + 1
                    File.write(f"Total Duplicate Files are :{Cnt1}\n")
                    Duplicate[checksum].append(fname)
                else:
                    Duplicate[checksum] = [fname]
                    File.write(f"Checksum fo Duplicated :{Duplicate[checksum]}\n")

        return Duplicate
        
    def DeleteDuplicate(self):
        File = Log()
        Boarder = "*"*50

        start_time = time.perf_counter()  
       
        t = datetime.datetime.now()

        File.write(f"{Boarder}\n\t\tAutomation Script Started\n{Boarder}\n")
        File.write(f"Starting Time of Directory Scanning is :{t}\n")

        myDict = self.FindDuplicate()

        end_time = time.perf_counter()

        Total_time_Scanned = end_time - start_time

        File.write(f"Completion time for Directory Scanning is : {Total_time_Scanned}\n")
        File.write(f"Name of Directory Scanned : {self.DirectoryPath}\n")

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
                    DeleteFiles = DeleteFiles + 1 
                    File.write(f"Total Number of Files Deleted : {DeleteFiles}\n")
                    File.write(f"Path of Duplicate Deleted File : {sub}\n")

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

        dobj = DeleteDuplicate(DirectoryName,ReceiverEmail)
        dobj.DeleteDuplicate()


    else:
        print(f'''Enter the Source Code as :
                pythonfile.py -h or -u for more information.''')

  

if __name__ == "__main__":
    main()