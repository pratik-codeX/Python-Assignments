from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

df = pd.read_csv("./student_performance_ml.csv")

df = pd.DataFrame(df)

X = df.drop(["FinalResult","SleepHours"],axis=1)

Y = df["FinalResult"]

print(df.shape)

checknull = df.isnull().sum()

for chk in checknull:
    if(chk == 1):
        df.dropna(how='all')

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

model = DecisionTreeClassifier(random_state=42)

model = model.fit(X_train,Y_train)

y_pred = model.predict(X_test)

print("Accuracy is : ",accuracy_score(Y_test,y_pred)*100)