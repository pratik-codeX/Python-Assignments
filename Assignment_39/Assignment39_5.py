'''
5. Calculate:
•Training accuracy
•Testing accuracy
Compare both and comment whether the model is overfitting or underfitting.
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

    model = DecisionTreeClassifier()

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    trained_model = model.fit(X_train,Y_train)

    Y_pred = trained_model.predict(X_test)

    result = accuracy_score(Y_test,Y_pred)
   
    print(result*100)
    print(Y.unique())

    cm = confusion_matrix(Y_test,Y_pred)
    #print(cm)

    Display_Confusion_Matrix = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["Fail","Pass"])

    print(X_train.shape)
    print(Y_train.shape)
    
    print(X_test.shape)
    print(Y_test.shape)
    print(Y_pred.shape)

    train_accuracy = trained_model.score(X_train,Y_train) * 100
    testing_accuracy = trained_model.score(X_test,Y_pred) * 100
    print("X test :",X_test)
    print("Y test : ",Y_test)

    print("Training Accuracy is :",train_accuracy)
    print("Testing Accuracy is :",testing_accuracy)
    
    Display_Confusion_Matrix.plot()
    plt.show()

def main():
    ClassificationX()


if __name__ == "__main__":
    main()