#4. Create a new DataFrame with details of 5 new students.
#Use the trained model to predict their results.
#Display predictions clearly.

import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("./student_performance_ml.csv")

df = pd.DataFrame(df)

X = df.drop("FinalResult",axis = 1)
Y = df["FinalResult"]


test = pd.DataFrame({
                        "StudyHours":[2.0,3.0,2.0,5.0,4.5],
                        "Attendance":[65,50,49,80,49],
                        "PreviousScore":[45,35,60,70,55],
                        "AssignmentsCompleted":[3,6,7,9,5],
                        "SleepHours":[5,7,6,8,4]
                    })

#print("features are X : \n",X)
#print("features are Y : \n",Y)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

print("X train is : \n",X_train.shape)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,Y_train)

y_pred = model.predict(test)

print("Prediction is : ",y_pred)
