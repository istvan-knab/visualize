import yaml
from plot_types import *
from plot_types.heatmap import Heatmap

if __name__ == "__main__":

    with open("misc/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    plot = Heatmap(config["PATH"])
    plot.create_plot()
    plot.visual_appearance()
