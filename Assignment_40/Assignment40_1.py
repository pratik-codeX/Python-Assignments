from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

df = pd.read_csv("./student_performance_ml.csv")

df = pd.DataFrame(df)

X = df.drop(["FinalResult"],axis=1)

Y = df["FinalResult"]

print(df.shape)

checknull = df.isnull().sum()

for chk in checknull:
    if(chk == 1):
        df.dropna(how='all')

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

model = DecisionTreeClassifier()

model = model.fit(X_train,Y_train)

Count = 0
for i in model.feature_importances_:
    Count += 1
    if i == 1:
        print(f"Feature {model.feature_names_in_[Count]} has more importance  i.e. {i*100}")