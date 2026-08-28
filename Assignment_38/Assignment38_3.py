import pandas as pd

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print(Boarder)
    print("Average StudyHours :  : ",df["StudyHours"].mean())

    print(Boarder)
    print("Average Attendance :  : ",df["Attendance"].mean())

    
    print(Boarder)
    print("Maximum PreviousScore :  : ",df["PreviousScore"].max())

    print(Boarder)
    print("Maximum PreviousScore :  : ",df["SleepHours"].min())
        

if __name__ == "__main__":
    main()