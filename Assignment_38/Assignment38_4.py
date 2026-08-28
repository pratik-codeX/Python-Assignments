#4. Use value_counts() to analyze the distribution of FinalResult.
#Calculate the percentage of Pass and Fail students.
#Is the dataset balanced? Justify your answer.

import pandas as pd

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    #print(df["FinalResult"].value_counts())
   
    result = df["FinalResult"].value_counts()

    StudentCount = len(df["FinalResult"])
    Flag = False

    Finalresultlist = df["FinalResult"].tolist()

    CountPass = 0
    CountFail = 0

    for data in Finalresultlist:
        if data == 1:
            CountPass += 1
        else:
            CountFail += 1

    
    print("Distribution of FinalResult Column")
    print(result)
    print(f"Percentage of Pass Student is : {(CountPass/StudentCount)*100}")
    print(f"Percentage of Fail Student is : {(CountFail/StudentCount)*100}")

    if((CountPass/StudentCount)*100) != 50.0 :
        print("Data Set is not Balanced")
    

        
    

if __name__ == "__main__":
    main()