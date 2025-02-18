#!/usr/bin/env python3

# Visualization with Plotly Express
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("BES2.csv")

# Add "leave_column" column
df["leave_column"] = df["vote"].apply(
    lambda x: True if x == "leave" else (False if x == "stay" else None)
)

# Add "age_group" column
bins = [0, 29, 60, float("inf")]
labels = ["young", "mid-life", "old"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=True)

# Visualization: Distribution of Age Groups
fig1 = px.histogram(
    df,
    x="age_group",
    title="Distribution of Age Groups",
    color_discrete_sequence=["#636EFA"],
)
fig1.write_image("age_group_distribution.png")
fig1.show()

# Visualization: Leave Votes by Age Group
fig2 = px.histogram(
    df,
    x="age_group",
    color="leave_column",
    barmode="group",
    title="Leave Votes by Age Group",
    color_discrete_sequence=["#EF553B", "#00CC96"],
)
fig2.write_image("leave_votes_by_age_group.png")
fig2.show()

# Visualization: Leave Votes by Education Level
fig3 = px.histogram(
    df,
    x="education",
    color="leave_column",
    barmode="group",
    title="Leave Votes by Education Level",
    color_discrete_sequence=["#EF553B", "#00CC96"],
)
fig3.write_image("leave_votes_by_education.png")
fig3.show()

print("Visualizations have been generated and saved as images.")
