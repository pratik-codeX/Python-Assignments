import schedule
import time
import datetime

def Task():

    file = open("Marvellous.txt","+a")
    date = datetime.datetime.now()

    file.write(f"Task Executed :{date}"+"\n")

def main():
    print("Automation Script Started...")

    schedule.every(1).second.do(Task)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()