'''
2: Write a Python program that monitors the size of a specifcied file
every 30 seconds.
Write the following details into:
FileSizeLog.txt
•File path
•File size in bytes
•Date and time
Handle the situation where the file does not exist.
'''

import schedule
import datetime
import os

def monitor_file(Filename):

    if os.path.exists(Filename) == False:
        print("File Does not Exist in this Directory")
        return
    
    fname = open(Filename,"r")

    dobj = datetime.datetime.now()

    fobj = fname.seek(0,2)
    date_time = dobj.strftime("%d-%m-%Y and %I:%M")
    print(f"File Size is :{fobj} bytes")

def main():

    FilePath = input("Enter path : ")
    Fname = input("Enter File Name :")
    Flag = True


    
    for DirName,SubDir,FileName in os.walk(FilePath):
        for fname in FileName:
            if os.path.exists(fname) == Flag:
                monitor_file(Fname)
            else:
                Flag = False

    if Flag == False:
        print("File Does not Exist")
                
    #print("Automation Script Started...")

    #schedule.every(5).minutes.do(monitor_file)

    #while(True):
        #  schedule.run_pending()

        #time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()