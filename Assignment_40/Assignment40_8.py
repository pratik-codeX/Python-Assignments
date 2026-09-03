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

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.8)

model = DecisionTreeClassifier(random_state=0)

model = model.fit(X_train,Y_train)

y_pred = model.predict(X_test)

print("Y pred is : ",y_pred)
print("Values of Y_test are : \n",Y_test.values)

print("X test : ",X_test)
print("Values of Y_pred are :\n",y_pred)


print("Accuracy is : ",accuracy_score(Y_test,y_pred)*100)

#the Accuracy that generated at 0 is 50 to 95
#the Accuracy that generated at 10 is 90 to 100
#the Accuracy that generated at 42 is mostly 100 and fluctuates between 90 