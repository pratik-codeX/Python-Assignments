import schedule
import time
import datetime

def LunchBreak():
    print(" LunchBreak !")

def WrapupWork():
    print("Wrap up work")

def main():
    print("Automation Script Started...")


    schedule.every().day.at("13:00").do(LunchBreak)
    schedule.every().day.at("18:00").do(WrapupWork)
    
    
    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()