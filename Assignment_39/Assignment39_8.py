import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay

class MLopsPipeline:
    #-------------------------------------------------------------
    #   Class Variable
    #-------------------------------------------------------------
    DataPath = "./student_performance_ml.csv"

    def __init__(self,DataPath):    #Constructor 
        self.Boarder = "-"*100  
        
        self.DataPath = DataPath    #initializes the Dataset for class 
    
    ########################################################
    #   Step 1 : Load the Dataset
    ########################################################

    #--------------------------------------------------------------
    #   Function Name : LoadtheData
    #   Description   : It load the dataset
    #   Input         : self
    #   Output        : None
    #   Author        : Pratik Nanaso Raut
    #   Date          : 19/8/2026
    #--------------------------------------------------------------
    def LoadtheData(self):
        DataFrame = pd.read_csv(self.DataPath)  

        print("Data Loaded Succesfully")

        return DataFrame

    ########################################################
    #   Step 2 : Data Analysis 
    ########################################################
    
    #--------------------------------------------------------------
    #   Function Name : DataAnalysis
    #   Description   : Analyze the data
    #   Input         : self
    #   Output        : None
    #   Author        : Pratik Nanaso Raut
    #   Date          : 19/8/2026
    #--------------------------------------------------------------
    def DataAnalysis(self):
        print(self.Boarder)
        print("Data Analysis")
        print(self.Boarder)
        df = self.LoadtheData()

        print(self.Boarder)
        print(df.head())
        print(self.Boarder)

        print(df.tail())
        print(self.Boarder)
        #df = df.drop()

        #DataFrame R*C
        #print("Rows and Columns",df.shape)
        #print("Columns name : :\n",list(df.columns))
        #print("Data of Dataset :\n",(df.values))

        print(df.value_counts())
        print(self.Boarder)

        print(df.info())
        print(self.Boarder)

        print(df.shape)
        print(self.Boarder)

        if df.empty == True:
            print("DataSet is Empty")
            return
        elif df.isnull().values.any():
            print("Data frame have null")
            df.dropna(inplace=True)

        print("Data Analyzed Successfully")

        return df

    ##########################################################
    #   Step 3 : Visualization
    ##########################################################
       
    #--------------------------------------------------------------
    #   Function Name : Visualization
    #   Description   : Visualize the data
    #   Input         : self
    #   Output        : None
    #   Author        : Pratik Nanaso Raut
    #   Date          : 19/8/2026
    #--------------------------------------------------------------
    def Visualization(self):
        print(self.Boarder)
        print("Data Visualization")

        df = self.DataAnalysis()    #return dataset

        features = [        #features of the dataframe
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
        ]

        fig,axes = plt.subplots(
            2,3,
            figsize=(12,8)
        )

        axes = axes.flatten()

        for i,feature in enumerate(features): # gives index as well as value of that index in iterable object as enumerate 

            sns.boxplot(        #boxplot for better visualization of data as there is multiple features and binary classification
                data=df,        #data according to features and labels
                x="FinalResult",#label
                y=feature,      #features of dataframe
                ax=axes[i]      # axes of plot
            )

            axes[i].set_title(f"{feature} vs FinalResult")
            axes[i].set_xlabel("Final Result")
            axes[i].set_ylabel(feature)

        fig.suptitle("Features vs FinalResult")
        # Hide the unused 6th subplot
        axes[5].set_visible(False)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    #############################################################
    #   Step 4 : Training and Testing of model with Evaluation
    #############################################################

        #--------------------------------------------------------------
        #   Function Name : TrainModel
        #   Description   : Train the model, Test the model
        #                   Generate the Confusion matic and Display it.
        #   Input         : self
        #   Output        : None
        #   Author        : Pratik Nanaso Raut
        #   Date          : 19/8/2026
        #--------------------------------------------------------------
    def TrainModel(self):
        df = self.DataAnalysis()

        X = df.drop("FinalResult",axis = 1) 
        Y = df["FinalResult"]

        test = np.array([5,65,45,5,5])  
        test = test.reshape(1,5)
        test_series = pd.DataFrame(test,columns=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"])

        model = DecisionTreeClassifier(max_depth=5)
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

        model = model.fit(X_train,Y_train)
        Y_pred = model.predict(X_test)

        predict1 = model.predict(test_series)

        print("Accuracy of model is : ",accuracy_score(Y_test,Y_pred)*100)
        print("Confusion Matix : \n",confusion_matrix(Y_test,Y_pred))

        cm = confusion_matrix(Y_test,Y_pred)

        display = ConfusionMatrixDisplay(confusion_matrix=cm)

        display.plot()

        plt.show()


def main():
    ml = MLopsPipeline("./student_performance_ml.csv")

    #ml.DataAnalysis()
    #ml.Visualization()
    ml.TrainModel()

if __name__ == "__main__":
    main()