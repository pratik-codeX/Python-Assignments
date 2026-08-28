#10. Plot SleepHours against FinalResult.
#Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    X = df["SleepHours"]
    Y = df["FinalResult"]

    for sp in df["FinalResult"].unique():
            temp = df[df["FinalResult"] == sp]
            plt.scatter(X,Y,marker='.',s = 100,c='b',edgecolors="black",label="Pass = 1,Fail = 0")

    #plt.plot(X,color='black')
    plt.xlabel("Sleeping Hours")
    plt.ylabel("Students Final Result")

    plt.show()

if __name__ == "__main__":
    main()