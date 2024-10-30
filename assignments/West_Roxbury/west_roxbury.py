#!/usr/bin/env python3
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pyarrow.csv as csv
import pandas as pd
import plotly.express as px

table = csv.read_csv("WestRoxbury.csv")
df = table.to_pandas()
df.columns = df.columns.str.replace(" ", "_")

print(df.columns)

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
]

target = "TOTAL_VALUE_"

x = df[predictors]
y = df[target]

tmodel.fit(x, y)
y_pred = tmodel.predict(x)

print(r2_score(y, y_pred))

df_results = pd.DataFrame({"Actual": y, "Predicted": y_pred})


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
