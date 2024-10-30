#!/usr/bin/env python3
from sklearn import linear_model
from sklearn.metrics import r2_score
import pyarrow as pa
import pyarrow.csv as csv
import pandas as pd

table = csv.read_csv("toyota_corolla.csv")
df = table.to_pandas()

df2 = df.drop("Fuel_Type", axis=1)
df2.info()

tmodel = linear_model.LinearRegression()
predictors = [
    "Mfg_Month",
    "Mfg_Year",
    "KM",
    "HP",
    "Met_Color",
    "Automatic",
    "CC",
    "Doors",
    "Cylinders",
    "Weight",
    "Reg_Fee",
]

target = "Price"

print(predictors)

x = df2[predictors]
y = df2[target]

tmodel.fit(x, y)
y_pred = tmodel.predict(x)
score = r2_score(y, y_pred)
print(score)
