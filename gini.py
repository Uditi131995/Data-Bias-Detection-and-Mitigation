import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import KBinsDiscretizer



def gini(df):
    #make a deep copy of the original dataframe 
    dfCopy=df.copy(deep=True)
    #Dictionary to store all the results 
    result={}
    columns_name = dfCopy.columns.tolist()
    for feature in columns_name:
        #Check whether categorical or numerical features 
        x=dfCopy[feature].name in dfCopy.select_dtypes(include='O').columns
        #Categorical : Label Encoding 
        if(x==True):
          lbl_encode =preprocessing.LabelEncoder()
          dfCopy[feature]=lbl_encode.fit_transform(dfCopy[feature])
        else: 
           #Numerical : KBins Discretization 
           x = dfCopy[feature].to_numpy()
           attribute=x.reshape(-1,1)
           est = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
           est.fit(attribute)
           est.transform(attribute)

        numpy_array_feature = dfCopy[feature].to_numpy()
           #all values are treated equally, arrays must be 1d 
        array = numpy_array_feature.flatten()
           #"""Calculate the Gini coefficient of a numpy array."""
        if np.amin(array) <= 0:
              # Values cannot be negative:
           array -= np.amin(array)  
               # Values cannot be 0:
           array += 0
                #Values must be sorted:
           array = np.sort(array)
                # Index per array element:
           index = np.arange(1,array.shape[0]+1)
                # Number of array elements:
           n = array.shape[0]
                # Gini coefficient:
           result[feature]= [np.sum((2 * index - n  - 1) * array) / (n * np.sum(array))]

    return result

