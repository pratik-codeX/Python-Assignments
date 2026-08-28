#. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
#  Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    X = df["AssignmentsCompleted"]
    Y = df["FinalResult"]

    slope, intercept = np.polyfit(X, Y, 1)
    line = slope * X + intercept

    for sp in df["FinalResult"].unique():
            temp = df[df["FinalResult"] == sp]
            #print(temp["FinalResult"].any())
            if (temp["FinalResult"].any()) == True:
                plt.scatter(X,Y,marker='.',s = 100,c='b',edgecolors="black",label="Pass = 1,Fail = 0")
            else:
                plt.scatter(X,Y,marker='.',s = 100,c='w',edgecolors="black",label="Pass = 1,Fail = 0")

    #plt.plot(X,line,color='black')
    plt.xlabel("Students Assignments Completed")
    plt.ylabel("Students Final Result")

    plt.show()

if __name__ == "__main__":
    main()