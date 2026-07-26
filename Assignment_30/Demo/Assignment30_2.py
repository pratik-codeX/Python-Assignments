import schedule
import time
from datetime import datetime

def Display():
    now1 = datetime.now()    
    print("Date :",now1.day," and ",datetime.now())

def main():
    print("Automation Script Started...")

    schedule.every(2).seconds.do(Display)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()