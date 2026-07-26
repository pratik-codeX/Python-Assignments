import schedule
import time
import num2words

def DisplayMessage(message):
    print(message)

def main():

    message = input("Enter Message :")

    print("Automation Script Started...")

    schedule.every(5).seconds.do(DisplayMessage,message)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()