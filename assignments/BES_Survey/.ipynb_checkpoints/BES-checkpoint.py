#!/usr/bin/env python3
# Step 1: Wrangling the data
# BES_wrangle.py
import pandas as pd

# Load the dataset
input_file = "BES2.csv"
df = pd.read_csv(input_file)


# Add "leave" column
def map_leave(vote):
    if vote == "leave":
        return 1
    elif vote == "stay":
        return 0
    else:
        return float("nan")


df["leave"] = df["vote"].apply(map_leave)


# Add "agegrp" column
def categorize_age(age):
    if age < 35:
        return "young"
    elif 35 <= age <= 60:
        return "mid-life"
    else:
        return "senior"


df["agegrp"] = df["age"].apply(categorize_age)

# Save the wrangled data to a new file
output_file = "/mnt/data/BES2_p.csv"
df.to_csv(output_file, index=False)

print(f"Wrangled data saved to {output_file}")

# Step 2: Analyzing the data
# BES_analysis.py
import matplotlib.pyplot as plt
import seaborn as sns

# Load the wrangled dataset
df = pd.read_csv(output_file)

# Univariate analysis: Distribution of age groups
sns.countplot(data=df, x="agegrp", palette="viridis")
plt.title("Distribution of Age Groups")
plt.savefig("/mnt/data/age_groups.png")
plt.show()

# Bivariate analysis: Leave vs Age Group
sns.countplot(data=df, x="agegrp", hue="leave", palette="magma")
plt.title("Leave Votes by Age Group")
plt.savefig("/mnt/data/leave_by_age_group.png")
plt.show()

# Analysis by education level
sns.countplot(data=df, x="education", hue="leave", palette="cool")
plt.title("Leave Votes by Education Level")
plt.savefig("/mnt/data/leave_by_education.png")
plt.show()


# Summarize findings and visualizations in LaTeX
def generate_latex():
    latex_doc = r"""\documentclass{article}
\usepackage{graphicx}
\begin{document}

\title{Brexit Election Survey Analysis}
\author{}
\date{}
\maketitle

\section*{Introduction}
This document summarizes the findings of the analysis of the Brexit Election Survey data.

\section*{Findings}

\subsection*{Age Group Distribution}
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{age_groups.png}
    \caption{Distribution of Age Groups}
\end{figure}

\subsection*{Leave Votes by Age Group}
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{leave_by_age_group.png}
    \caption{Leave Votes by Age Group}
\end{figure}

\subsection*{Leave Votes by Education Level}
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{leave_by_education.png}
    \caption{Leave Votes by Education Level}
\end{figure}

\end{document}
"""
    latex_file = "/mnt/data/BES_analysis.tex"
    with open(latex_file, "w") as f:
        f.write(latex_doc)
    print(f"LaTeX document saved to {latex_file}")


generate_latex()
