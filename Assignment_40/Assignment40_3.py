from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

df = pd.read_csv("./student_performance_ml.csv")
dfX = pd.read_csv("./student_performance_ml.csv")

df1 = pd.DataFrame(df)
df2 = pd.DataFrame(dfX)

X = df1.drop(["FinalResult"],axis=1)
Y = df1["FinalResult"]

X1 = df2[["StudyHours","Attendance"]]
Y1 = df2["FinalResult"]

print("Shape of X1 ",X1.shape)
print("Shape of Y1 ",Y1.shape)
print("Shape of X ",X.shape)
print("Shape of Y ",Y.shape)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
X_train1,X_test1,Y_train1,Y_test1 = train_test_split(X1,Y1,test_size=0.2)

modelX = DecisionTreeClassifier(random_state=42)
modelDT = DecisionTreeClassifier(random_state=42)

modelX = modelX.fit(X_train,Y_train)
model1 = modelDT.fit(X_train1,Y_train1)

print("X features are : ",modelX.feature_names_in_)
print("X features are : ",model1.feature_names_in_)

y_pred = modelX.predict(X_test)
y_pred1 = model1.predict(X_test1)

print("Accuracy is : ",accuracy_score(Y_test,y_pred)*100)

print("With StudyHours and Attendance Accuracy is : ",accuracy_score(Y_test1,y_pred1)*100)


# There is no effect of removing other features 