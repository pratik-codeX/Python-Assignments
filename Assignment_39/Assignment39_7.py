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
import numpy as np

def ClassificationX():
    DataPath = "./student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]] 
    Y = df["FinalResult"]

    test_data = np.array([6,85,66,7,7]) #One Diamentianal array
    test_data = test_data.reshape(1,5)  #Converted into 2D array

    test_series = pd.DataFrame(test_data,columns=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"])

    model = DecisionTreeClassifier(max_depth=1,random_state=42)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    #print(X_test)
    #print("Test data :\n",test_data)

    try:
        model = model.fit(X_train,Y_train)  
    except Exception as eobj:
        print(eobj)    

    Y_pred = model.predict(test_series)       

    print(Y_pred)

    if(Y_pred == 1):
       print("Student is Passed")
    

def main():
    ClassificationX()


if __name__ == "__main__":
    main()