#   8. Draw a boxplot for Attendance.
#   Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt

def main():
    Boarder = "*"*50
    Dataset = "./student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    data = df["Attendance"]
    
    plt.boxplot(data)
    plt.title("Attendence Outlier")
    plt.show()

if __name__ == "__main__":
    main()