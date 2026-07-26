import schedule
import time
import datetime

def Display():
    print("Namskar..")

def main():
    print("Automation Script Started...")

    schedule.every().day.at("09:37").do(Display)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()