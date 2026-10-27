'''
10. Train model with    :   max_depth = None
Calculate:
•Training accuracy
•Testing accuracy
If training accuracy is 100% but testing accuracy is lower, explain why this happens.

'''

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np 

header = "-"*40
print(header)
print("Step 1 : Load the Dataset")
data = pd.read_csv("./student_performance_ml.csv")
print(header)
df = pd.DataFrame(data)

#PerIdx = (df["StudyHours"] * 2) + df["Attendance"]
#df["PerIdx"] = PerIdx

X = df.drop(["FinalResult"],axis=1)
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

model = DecisionTreeClassifier(random_state=42,max_depth = None)

model.fit(X_train,Y_train)

y_pred = model.predict(X_test)

print("Training accuracy is : ",model.score(X_train,Y_train)*100)
print("Testing accuracy is : ",model.score(X_test,Y_test)*100)


print("Accuracy is : ",accuracy_score(y_pred,Y_test)*100)
