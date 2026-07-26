import schedule
import time
import num2words

def Display(msg,time):
    print(msg)
    print(f"Every {num2words.num2words(time)} seconds.")

def main():

    message = input("Enter Message :")
    interval = int(input("Enter interval : "))

    if interval < 0:
        print("Invalid Interval : Error !")

    print("Automation Script Started...")

    schedule.every(interval).seconds.do(Display,message,interval)

    while(True):
        schedule.run_pending()

        time.sleep(1)

    print("End of Automation")

if __name__ == "__main__":
    main()