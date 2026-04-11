# this file is made for creating charts from the video

import pandas as pd
import datetime
import matplotlib.pyplot as plt
import os

class TrafficAnalyzer:
    def __init__(self, output_file="data/traffic_data.csv"):
        self.output_file = output_file

        #Ensure data folder exists
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

        #Load or cerate CSV file
        if os.path.exists(self.output_file):
            self.df = pd.read_csv(self.output_file)
        else:
            self.df = pd.DateFrame(columns=["time","vehicle_count"])
            self.df.to_csv(self.output_file, index=False)

    def log_data(self, vehicle_count):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        new_row = {
            "time" : current_time,
            "vehicle_count": vehicle_count
        }

        self.df = pd.concat([self.df, pd.DateFrame([new_row])], ignore_index=True)
        self.df.to_csv(self.output_file, index=False)

    def get_traffic_level(self, count):
        if count < 10:
            return "Low"
        elif count < 30:
            return "Medium"
        else:
            return "High"

    def plot_traffic(self):
        df = pd.read_csv(self.output_file)

        plt.figure()
        plt.plot(df["vehicle_count"])
        plt.xlabel("Time Index")
        plt.ylabel("Vehicle Count")
        plt.title("Traffic Analysis")
        plt.show()
