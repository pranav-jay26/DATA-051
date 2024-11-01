#!/usr/bin/env python3
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pyarrow.csv as csv
import pandas as pd
import plotly.express as px

table = csv.read_csv("WestRoxbury.csv")
df = table.to_pandas()
df.columns = df.columns.str.replace(" ", "_")
df_encoded = pd.get_dummies(df, columns=["REMODEL"])

print(df_encoded.columns)

tmodel = LinearRegression()

predictors = [
    "LOT_SQFT_",
    "YR_BUILT",
    "GROSS_AREA_",
    "LIVING_AREA",
    "FLOORS_",
    "ROOMS",
    "BEDROOMS_",
    "FULL_BATH",
    "HALF_BATH",
    "KITCHEN",
    "FIREPLACE",
    "REMODEL_None",
    "REMODEL_Old",
]

target = "TOTAL_VALUE_"

x = df_encoded[predictors]
y = df_encoded[target]

tmodel.fit(x, y)
y_baseline = tmodel.predict(x)

print(r2_score(y, y_baseline))

test_data = csv.read_csv("WRPredict.csv")
df_test = test_data.to_pandas()
df_test_encoded = pd.get_dummies(df_test, columns=["REMODEL"])
df_test_encoded.columns = df_test_encoded.columns.str.replace(" ", "_")
print(df_test_encoded.columns)

test_predictors = list(df_test_encoded.columns)
x_test = df_test_encoded[test_predictors]
y_test = tmodel.predict(x_test)
value_column = list(y_test)
df_test["TOTAL_VALUE"] = value_column
print(df_test)

df_results = pd.DataFrame({"Actual": y, "Predicted": y_baseline})

fig = px.scatter(
    df_results,
    x="Actual",
    y="Predicted",
    title="Actual vs Predicted Total Value",
    labels={"Actual": "Actual Total Value", "Predicted": "Predicted Total Value"},
)


fig.add_shape(
    type="line",
    x0=df_results["Actual"].min(),
    y0=df_results["Actual"].min(),
    x1=df_results["Actual"].max(),
    y1=df_results["Actual"].max(),
    line=dict(color="red", dash="dash"),
)

fig.show()
