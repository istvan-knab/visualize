import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def create_heatmap(matrix, title="Heatmap", cmap="viridis"):
    """
    Create a heatmap from a 4x4 matrix of double values.

    Args:
        matrix (list or np.ndarray): A 4x4 matrix of doubles (e.g., [[0.1, 0.2, 0.3, 0.4], ...])
        title (str): Title of the heatmap
        cmap (str): Color map for the heatmap (e.g., "viridis", "coolwarm", "Blues")
    """
    # Ensure the input is a 4x4 matrix
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        raise ValueError("Matrix must be 4x4")

    # Convert to DataFrame for Seaborn (optional but improves compatibility)
    df = pd.DataFrame(matrix)

    # Set up the plot
    plt.figure(figsize=(6, 5))  # Adjust size as needed
    sns.heatmap(
        df,
        annot=True,  # Show values in each cell
        fmt=".1f",  # Format numbers to 1 decimal place
        cmap=cmap,  # Color scheme
        cbar=True,  # Show color bar
        square=True,  # Make cells square
        linewidths=0.5,  # Add grid lines
    )



    # Add title
    plt.title(title)

    # Display the plot
    plt.show()


# Example 1: Using the 4x4 matrix of 0.1
matrix_ones = [[0.1 for _ in range(4)] for _ in range(4)]
create_heatmap(matrix_ones, title="Uniform 0.1 Heatmap", cmap="Blues")

# Example 2: A varied 4x4 matrix of doubles
nox_matrix= [
    [15578.5, 21155.625, 19727.166666666664, 36642.1875],
    [1967.0, 6241.875, 14461.166666666668, 3490.8125],
    [1907.25, 5979.0, 900.0, 5209.625],
    [3061.5, 9164.375, 13786.0, 8931.6875]
]

co2_matrix= [
    [9.696815221448484, 12.08690509406662 	, 10.953995795470462, 18.681152012423503 ],
    [3.174577057228829 	, 6.888747603416214 	, 11.06467797506226 , 4.529207252092852 ],
    [3.201523121191976 	, 7.031818083136436, 8.049265975442882 ,  6.072196617965197],
    [3.6138651794544283 	,  8.952280042963515 , 10.395977269377877 , 8.035374213475365 	]
]

input_matrix = co2_matrix
create_heatmap(input_matrix, title="CO2 Values", cmap="coolwarm")