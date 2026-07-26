import schedule
import sys
import os 
import shutil
from pathlib import Path
import datetime

def FileBackup(src_path,dest_path):
    dir = Path("Backup").mkdir()
    for Foldername,Subfolder,Filename in os.walk(src_path):
        for fname in Filename:
            fname = shutil.copy(fname,dir)
    
def main():
    print("Automation Script Started...")
    Dir  = ""   
    FileBackup("Demo",Dir)

    #src_path = sys.argv[1]
    #dest_path = sys.argv[2]

    #schedule.every(1).hour.do(FileBackup(src_path,dest_path))
    
   #while(True):
    #    schedule.run_pending()

     #   time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()