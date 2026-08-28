#7. Create a scatter plot of:
#StudyHours vs PreviousScore


import pandas as pd
import matplotlib.pyplot as plt

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    FeatCols = ["StudyHours","PreviousScore"]

    X = df[FeatCols]            
    Y = df["FinalResult"]

    #print("Shape of Feature Columns :",df[FeatCols])
    #print("Shape of Lable Column :",df["FinalResult"])

    for sp in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == sp]
        #print(temp["FinalResult"].any())
        if (temp["FinalResult"].any()) == True:
            plt.scatter(temp["PreviousScore"],temp["StudyHours"],marker='.',s = 100,c='b',edgecolors="black",label="Pass = 1,Fail = 0")
        else:
            plt.scatter(temp["PreviousScore"],temp["StudyHours"],marker='.',s = 100,c='w',edgecolors="black",label="Pass = 1,Fail = 0")
        

    '''plt.scatter(
        X,
        Y,
        s = 100,
        ,
        c='m',
        alpha=0.8,
        linewidths=0.5,
        edgecolors="black",
        label="Pass or Fail"
    )'''

    plt.title("Student Data")
    plt.xlabel("PreviousScore")
    plt.ylabel("StudyHours")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()