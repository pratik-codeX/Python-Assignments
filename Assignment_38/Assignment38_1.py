import pandas as pd

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print(Boarder)
    print("First five Entries:\n",df.head())
    print(Boarder)

    print(Boarder)
    print("Last five Entries :\n",df.tail())
    print(Boarder)

    print(Boarder)
    print("Number of Rows and Columns are :\n",df.shape)
    print(Boarder)

    print(Boarder)
    print("Columns are :\n",list(df.columns))
    print(Boarder)

    print("Datatype of : StudyHours : ",(df["StudyHours"].dtypes))
    print("Datatype of : Attendance : ",(df["Attendance"].dtypes))
    print("Datatype of : PreviousScore : ",(df["PreviousScore"].dtypes))
    print("Datatype of : AssignmentsCompleted : ",(df["AssignmentsCompleted"].dtypes))
    print("Datatype of : SleepHours : ",(df["SleepHours"].dtypes))
    print("Datatype of : FinalResult : ",(df["FinalResult"].dtypes))
    


if __name__ == "__main__":
    main()