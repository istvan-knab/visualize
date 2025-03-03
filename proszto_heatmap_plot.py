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


    # Set up the plot
    fig, ax = plt.subplots(figsize=(6, 5))  # Adjust size as needed
    sns.heatmap(
        matrix,
        annot=True,  # Show values in each cell
        fmt=".1f",  # Format numbers to 1 decimal place
        cmap=cmap,  # Color scheme
        cbar=True,  # Show color bar
        square=True,  # Make cells square
        linewidths=0.5,  # Add grid lines
    )
    plt.xlabel("Test Network Size", size="x-large")
    plt.ylabel("Training Network Size", size="x-large")

    ax.set_xticklabels([1, 2, 3, 4])
    ax.set_yticklabels([1, 2, 3, 4], rotation=0)


    # Add title
    plt.title(title, size="x-large")

    # Display the plot
    plt.show()


# Example 1: Using the 4x4 matrix of 0.1
matrix_ones = [[0.1 for _ in range(4)] for _ in range(4)]
create_heatmap(matrix_ones, title="Uniform 0.1 Heatmap", cmap="Blues")

# Example 2: A varied 4x4 matrix of doubles
waiting = pd.read_csv("/home/sztaki/Documents/visualize/data/waiting.csv", header=None)
waiting = pd.DataFrame(waiting)

create_heatmap(waiting, title="Waiting Time", cmap="coolwarm")