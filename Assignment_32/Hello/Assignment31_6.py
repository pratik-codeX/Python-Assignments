'''
6: Write a program that schedules the following messages:
•Monday at 9:00 AM: Start your weekly goals
•Wednesday at 5:00 PM: Review your weekly progress
•Friday at 6:00 PM: Weekly work completed
Use:
schedule.every().monday.at(...)
schedule.every().wednesday.at(...)
schedule.every().friday.at(...)
'''

import schedule
import time


def MessageatMonday():
    print("Start Your Weekly Goals")

def MessageatWednesday():
    print("Review your Weekly process")

def MessageatFriday():
    print("Weekly work completed")
    
def main():

    print("Automation Script Started...")

    schedule.every(1).monday.do(MessageatMonday)
    schedule.every(1).wednesday.do(MessageatWednesday)
    schedule.every(1).friday.do(MessageatFriday)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()