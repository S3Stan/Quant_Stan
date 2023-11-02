# imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt



# constants 



# APi endpoints


# datafile URL
creditcardData = pd.read_csv("Datasets/creditcard.csv" , sep=",")

# exception to catch what happens when dataset is called 
class datasetNotFoundException(Exception):
    pass # what does this mean?????

# imports 
def sendCreditCardData():
    creditcardData
    
    return creditcardData



# def sendImportLibrary():

#     # send import data    
#     import numpy as np
#     import pandas as pd
#     import matplotlib.pyplot as plt
#     import pandas as pd
#     #from sklearn.model_selection import train_test_split
#     from sklearn.tree import DecisionTreeClassifier
#     from sklearn.metrics import accuracy_score, confusion_matrix
    
#     return np, pd, plt,DecisionTreeClassifier, accuracy_score, confusion_matrix ""


    
# dataset imports pd.read_csv("laptop_repair.txt", sep=" ")

    
    
#creditcardData.info()