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

model = DecisionTreeClassifier(random_state=42)

model = model.fit(X_train,Y_train)

y_pred = model.predict(X_test)

print("Y pred is : ",y_pred)
print("Values of Y_test are : \n",Y_test.values)

#print("X test : ",X_test)
#print("Values of Y_pred are :\n",y_pred)

for 


cnt = 0
flag = 0
for i in Y_test.values:
    if i != y_pred[cnt]:
        print("Miss Classified Row is : ",X_test)
    cnt = cnt+1

#print("User defined Accuracy is : ",(flag / len(Y_test)) * 100)

#print("Accuracy is : ",accuracy_score(Y_test,y_pred))