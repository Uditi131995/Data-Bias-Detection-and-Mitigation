import copy
from sklearn.preprocessing import KBinsDiscretizer
from sklearn import preprocessing

def data_encoding(df):
    #Deep copy
   df_copy=copy.deepcopy(df) 
   #Drop the null columns 
   df_copy=df_copy.dropna()
   colm_nm = df_copy.columns.tolist()
   #print(colm_nm)
   for i in colm_nm :
       #print(df[i].name in df.select_dtypes(include="O").columns)
       if df[i].name in df.select_dtypes(include="O").columns:
            lbl_encode =preprocessing.LabelEncoder()
            df_copy[i]=lbl_encode.fit_transform(df_copy[i])
            print(df_copy[i])
        
         
       else: 
           pass   
        #    print(df_copy[i])
        #    print(df_copy[i].info())
        #    est = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
        #    print(est.fit_transform(df_copy[i]))
        #    #print(est.transform(df_copy[i]))
        #    exit() 
        


       


