#   Generate confusion matrix using sklearn.
#   Display it using ConfusionMatrixDisplay.
#   Explain clearly:
#   •True Positive
#   •True Negative
#   •False Positive
#   •False Negative

from sklearn.tree import DecisionTreeClassifier 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
import matplotlib.pyplot as plt

def ClassificationX():
    DataPath = "./student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]] 
    Y = df["FinalResult"]

    model = DecisionTreeClassifier()

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    result = accuracy_score(Y_test,Y_pred)
   
    print(result*100)
    print(Y.unique())

    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)

    Display_Confusion_Matrix = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["Fail","Pass"])

    Display_Confusion_Matrix.plot()
    plt.show()

def main():
    ClassificationX()


if __name__ == "__main__":
    main()