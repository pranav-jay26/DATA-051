#!/usr/bin/env python3

from pyarrow import csv
import plotly.express as px

table = csv.read_csv("train.csv")
age_values = table["Age"].to_pylist()
sex_values = table["Sex"].to_pylist()
print(table)
# Create a histogram using Plotly Express
fig = px.histogram(x=age_values, color=sex_values)
fig.show()
