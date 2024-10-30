#!/usr/bin/env python3

import pandas as pd
import pyarrow as pa
import pyarrow.csv as csv
import pyarrow.compute as pc
import numpy as np
import plotly.express as px

table = csv.read_csv("PIN_Data.csv")
df = table.to_pandas()


def first_two_digits(num: int) -> int:
    num = abs(num)
    num_str = str(num)
    if 2 >= num:
        return int(num)
    else:
        return int(num_str[:2])


def last_two_digits(num: int) -> int:
    num = abs(num)
    num_str = str(num)
    if 2 >= num:
        return num
    else:
        return int(num_str[-2:])


if __name__ == "__main__":
    df["first_two"] = df["PIN"].map(first_two_digits)
    df["last_two"] = df["PIN"].map(last_two_digits)
    print(df)

    frequency_matrix = np.zeros((100, 100))

    for _, row in df.iterrows():
        first = row["first_two"]
        last = row["last_two"]
        frequency_matrix[first, last] += 1

    log_frequency_matrix = np.log10(frequency_matrix)

    frequency_df = pd.DataFrame(log_frequency_matrix)

    fig = px.imshow(
        frequency_df,
        labels=dict(
            x="Frequency of First Two Digits",
            y="Frequency of Last Two Digits",
            color="Frequency",
        ),
        x=[f"{i}" for i in range(100)],  # Labels for x-axis
        y=[f"{i}" for i in range(100)],  # Labels for y-axis
        title="Heatmap of Frequency of First and Last Two Digits",
    )

    fig.show()
