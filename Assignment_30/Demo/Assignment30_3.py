import schedule
import time
import datetime

def Display():
    print("Coding kar...!")

def main():
    print("Automation Script Started...")

    schedule.every(30).minutes.do(Display)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()