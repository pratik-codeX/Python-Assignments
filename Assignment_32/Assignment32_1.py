import schedule
from datetime import datetime
import time

def WriteFile():
    tobj = datetime.now()
    curr_date = tobj.strftime("%d-%m-%y")
    curr_time = tobj.strftime("%I:%M:%p")

    fname = tobj.strftime("File_"+"%d_%m_%y_%I_%M_%S"+".txt")
    
    fobj = open(fname,"a")
    fobj.write(f"File Name : {fname}\n Creation date : {curr_date}\n Creation time : {curr_time} \n")

def main():
    print("Automation Script Started...")

    schedule.every(1).minutes.do(WriteFile)

    while(True):

        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()