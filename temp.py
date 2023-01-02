import pandas as pd
import numpy as np
import seaborn as sns
# we add this for partition the data
from sklearn.model_selection import train_test_split #Library
# we add this for Logistic Regression
from sklearn.linear_model import LogisticRegression  #Library

# we import performence matrix, accurcy score & confusion matrix
from sklearn.metrics import accuracy_score, confusion_matrix
#Importing the Data
too=pd.read_csv("./income.csv")
tot = too.copy()
# geting to know our Data
print(tot.head(5))
print(tot.info())
print("Data whit missing Value:\n",tot.isnull().sum())
# get the summary of missing value
print("Statical spesfied:\n",tot.describe())

# summary of Catagorical Variable
#summary_data = tot.describe(include = "O")
#print("this is new Line and the result is after that: \n",summary_data)

# get the count of each column:
tot.head(3)
tot["JobType"].value_counts()
print("this is a new line: ")
tot["occupation"].value_counts()



# Chicking for uniqe charectar:

print(np.unique(tot["JobType"])) 




# by run the up line code we know which we have nan value in JobType and 
     # Occupation and now by the adding the na_value= "?" we want to represent
     # that to black.
    
too = pd.read_csv("income.csv",na_values=" ?")
tot =too.copy()
tot.isnull().sum()

missing = tot[tot.isnull().any(axis=1)]

#now we delete the missing data becuse we dont have any relation ship betwen them.

tot1=tot.dropna(axis=0)
tot = tot1.copy()


tot.isnull().sum()
tot["JobType"].value_counts()

corrlation = tot.corr()

# get the title of each Column
tot.columns


#Get the count of Gender
gender = pd.crosstab(index = tot["gender"],
                     columns="count",
                     normalize= True
                     )


print(gender)


# get the Salary and relation ship of that whit gender

sal = pd.crosstab( index =tot["gender"],
                   columns=tot["SalStat"],
                   margins=True,
                   normalize = "index")


print(sal)


















