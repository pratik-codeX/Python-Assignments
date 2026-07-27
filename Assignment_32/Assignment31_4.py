'''
4: Write a program that creates a new log le after every ten minutes.
The lename should contain the current date and time.
Example:
MarvellousLog_25_07_2026_16_30_00.txt
The le should contain:
Log file created successfully.
Creation Time: 25-07-2026 04:30:00 PM
'''

import schedule
import datetime
import time
import os

def CreateLogFile():

    tobj = datetime.datetime.now()
    FileName = tobj.strftime("%d-%m-%y %I:%M:%S %p")
    FileName = FileName.replace("-","_")        
    FileName = FileName.replace(":","_")

    fobj = open(FileName,"a")

    format_Time = tobj.strftime("%d-%m-%y %I:%M:%S %p")

 

def main():

    tobj = datetime.datetime.now()
    FileName = tobj.strftime("%d-%m-%y %I:%M:%S %p")
    FileName = FileName.replace("-","_")
    FileName = FileName.replace(":","_")
    FileName = FileName.replace(" ","_")
    print(FileName)

    print("Automation Script Started...")

    schedule.every(10).minutes.do(CreateLogFile)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()