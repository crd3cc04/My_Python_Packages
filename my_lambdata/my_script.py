# now its my_lambdata/my_script.py or -m my_lambdata.my_script
# this file is for actual code execution
from my_lambdata.my_mod import enlarge
x = 10
print("ENLARGE", x, "TO",  enlarge(x))

import pandas as pd
import numpy as np

print("happy tuesday night.")

colors =  {"Green":[np.nan,2,3], 
           "Red":[3,4, np.nan]}


# Looking for null values
df = pd.DataFrame(colors)
print(df.head())

# Getting report of null values
df.notnull()
print(df.head())

# Train/Test 
#import sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(df, test_size=0.2)
#print(X_train.shape, y_train.shape)
#print(X_test.shape, y_test.shape)

#Train/validation/test split
#train, val = train_test_split(train, train_size=0.80, test_size=0.20,
                              #random_state=42)