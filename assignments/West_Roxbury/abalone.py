#!/usr/bin/env python3
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pyarrow.csv as csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load and prepare data
table = csv.read_csv("abalone.csv")
df = table.to_pandas()
print(df.columns)

df2 = df.drop("Sex", axis=1)
df2.info()

model = LinearRegression()
predictors = [
    "Length",
    "Diameter",
    "Height",
    "Whole Weight",
    "Shucked Weight",
    "Viscera Weight",
    "Shell Weight",
]

target = "Rings-Age"

x = df2[predictors]
y = df2[target]

# Train the model and make predictions
model.fit(x, y)
y_pred = model.predict(x)

# Print R-squared score
print(r2_score(y, y_pred))

# Prepare results DataFrame and correlation matrix
df_results = pd.DataFrame({"Actual": y, "Predicted": y_pred})
correlation_matrix = df2.corr()
numpy_matrix = correlation_matrix.values

# Create subplots with 1 row and 2 columns
fig = make_subplots(
    rows=1, cols=2, subplot_titles=("Actual vs Predicted", "Correlation Heatmap")
)

# Scatter plot for actual vs predicted
scatter_trace = go.Scatter(
    x=df_results["Actual"],
    y=df_results["Predicted"],
    mode="markers",
    name="Predictions",
)
fig.add_trace(scatter_trace, row=1, col=1)

# Add line of equality to scatter plot
fig.add_shape(
    type="line",
    x0=df_results["Actual"].min(),
    y0=df_results["Actual"].min(),
    x1=df_results["Actual"].max(),
    y1=df_results["Actual"].max(),
    line=dict(color="red", dash="dash"),
    row=1,
    col=1,
)

# Heatmap for the correlation matrix
heatmap_trace = go.Heatmap(
    z=numpy_matrix,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorbar=dict(title="Correlation"),
)
fig.add_trace(heatmap_trace, row=1, col=2)

# Update layout
fig.update_layout(title="Actual vs Predicted Age and Correlation Heatmap")

# Show combined plot
fig.show()
