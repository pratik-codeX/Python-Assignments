#4. Create a new DataFrame with details of 5 new students.
#Use the trained model to predict their results.
#Display predictions clearly.

import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv("./student_performance_ml.csv")

df = pd.DataFrame(df)

X = df.drop("FinalResult",axis = 1)
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.8)

result = DecisionTreeClassifier(random_state=42)

model = result.fit(X_train,Y_train)

y_pred = model.predict(X_test)

print("Y pred is : ",y_pred)
print("Values of Y_test are : \n",Y_test.values)

print("X test : ",X_test)
print("Values of Y_pred are :\n",y_pred)

print("Accuracy is : ",accuracy_score(Y_test,y_pred)*100)

fig = plt.figure(figsize = (10,5))

plot_tree(result,feature_names=list(X.columns),filled=True,label='root',max_depth=10,fontsize=10)

plt.show()