'''
6. Train three Decision Tree models with:
•max_depth = 1
•max_depth = 3
•max_depth = None
Compare their testing accuracies and write your observations.
'''

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

    model1 = DecisionTreeClassifier(max_depth=1,random_state=42)
    model2 = DecisionTreeClassifier(max_depth=2,random_state=42)
    model3 = DecisionTreeClassifier(max_depth=None,random_state=42)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    trained_model1 = model1.fit(X_train,Y_train)
    trained_model2 = model2.fit(X_train,Y_train)
    trained_model3 = model3.fit(X_train,Y_train)

    Y_pred1 = trained_model1.predict(X_test)
    Y_pred2 = trained_model2.predict(X_test)
    Y_pred3 = trained_model3.predict(X_test)

    result1 = accuracy_score(Y_test,Y_pred1)
    result2 = accuracy_score(Y_test,Y_pred2)
    result3 = accuracy_score(Y_test,Y_pred3)

    print(result1*100)
    print(result2*100)
    print(result3*100)

def main():
    ClassificationX()


if __name__ == "__main__":
    main()