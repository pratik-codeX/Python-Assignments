#   1. Import DecisionTreeClassi er from sklearn.
#   Create a model object and train it using fit().

from sklearn.tree import DecisionTreeClassifier 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

def main():
    ClassificationX()


if __name__ == "__main__":
    main()