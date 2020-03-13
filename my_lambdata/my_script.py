# now its my_lambdata/my_script.py

import pandas as pd
print("happy tuesday night.")

df = pd.DataFrame ({"Green":[1,2,3], "Red":[3,4,5]})
print(df.head())

# Looking for null values
#df.isnull

# Getting report of null values
#df.isnull().sum()

# Train/Test 
#import sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(df, test_size=0.2)
#print(X_train.shape, y_train.shape)
#print(X_test.shape, y_test.shape)

#Train/validation/test split
#train, val = train_test_split(train, train_size=0.80, test_size=0.20,
                              #random_state=42)