#!/usr/bin/env python3
import pandas as pd

df = pd.read_csv("multidata.csv")
# print(df.head(5))

filtered_df = df["dataset"] == "A"

print(filtered_df)
