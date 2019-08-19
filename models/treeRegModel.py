# Predicting the cost of an Airbnb by factors such as location, reviews, minimum night stay and more

#import pandas and sklearn
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

#Read the data
data=pd.read_csv('../data/raw/listings.csv')

#Set up target  and predicting variable
y = data.price
X = data.drop(['price','name','host_name','last_review','host_id','id'],axis=1)

# Divide data into training and validation subsets
X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, random_state=1)

# Select categorical columns
categorical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# Keep selected columns only
my_cols = categorical_cols + numerical_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()


# Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='mean')

#Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundle preprocessing for categorical data
preprocessor = ColumnTransformer(transformers =[
    ('num',numerical_transformer,numerical_cols),
    ('cat', categorical_transformer, categorical_cols)
])

# create forest model
model = RandomForestRegressor(random_state=1)

# Bundle preprocessing and modeling code in a pipeline
my_pipeline = Pipeline(steps=[('preprocessor',preprocessor),('model',model)])

# Train the model and have it perform predictions.
tic = time.clock()
my_pipeline.fit(X_train, y_train)
predictions = my_pipeline.predict(X_valid)

# Print results and timings
print(mean_absolute_error(y_valid, predictions))
print(time.clock()-tic)

