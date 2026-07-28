import schedule
import datetime
import time
import os
from pathlib import Path

def CopyFiles(file,Dest):
    fobj = open(file,"r")
        
    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        if os.path.exists(Dest) == False:
            os.mkdir(Dest)
        filename = os.path.basename(file)
        n = os.path.join(Dest,filename)
        fobj1 = open(n,"a+")
        fobj1.write(Buffer)
        Buffer = fobj1.read(1024)

def ContentCopy(SourceDir,DestDir):
    Flag = False

    ret = os.path.exists(SourceDir)
    if ret == False:
        print("Source Directory Does not Exists")
        return
    
    for Dirname,Subdir,Filename in os.walk(SourceDir):
            for fname in Filename:
                fname = os.path.join(Dirname,fname)
                extension = Path(fname)
                if extension.suffix == ".txt":
                    CopyFiles(fname,DestDir)
                    logfile = open("CopiedFile.log","a+")
                    logfile.write(f"Copied file are :{os.path.basename(fname)}\n")

def main():

    Source = input("Enter Source Directory :")
    Desti = input("Enter Destination Directory : ")
    print("Automation Script Started...")

    schedule.every(1).seconds.do(ContentCopy,Source,Desti)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")
    
if __name__ == "__main__":
    main()