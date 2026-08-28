import pandas as pd

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print(Boarder)
    print("Total Number of Students in dataset : ",len(df.index))

    FailedCount = 0
    for i in df["FinalResult"].tolist():
        if i == 0:
            FailedCount += 1

    print(Boarder)
    print("Total Failed Student : ",FailedCount)

    print(Boarder)
    print("Total Passed Students : ",len(df.index) - FailedCount)




if __name__ == "__main__":
    main()