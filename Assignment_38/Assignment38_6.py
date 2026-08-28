#6. Plot a histogram of StudyHours.
#Explain what the distribution tells you


import pandas as pd
import matplotlib.pyplot as plt

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    x = df["StudyHours"]

    plt.hist(
        x,
        bins=5,
        edgecolor="black",
        alpha= 0.9,
        rwidth=0.5 
    )

    plt.title("Student Performance Analysis")
    plt.xlabel("StudyHours")
    plt.ylabel("Students")
    
    plt.show()
    

if __name__ == "__main__":
    main()