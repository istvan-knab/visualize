import csv
import pandas as pd

class BaseVisualClass:
    def __init__(self,data_path:str) -> None:

        with open(data_path, 'r') as file:
            data = csv.reader(file)
            self.data = pd.DataFrame(data)

    def create_plot(self):
        pass

    def visual_appearance(self):
        pass
