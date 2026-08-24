#4. Create a new DataFrame with details of 5 new students.
#Use the trained model to predict their results.
#Display predictions clearly.

import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split


df = pd.read_csv("./student_performance_ml.csv")

X = df.drop(["FinalResult"],axis = 1)
Y = df["FinalResult"]

#print("features are X : \n",X)
#print("features are Y : \n",Y)

X_train,X_test_Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

print("X train is : \n",X_train)