# This file is made for driver to help each other on based of the traffic level
# IDEA TODO -> make the chatbot take more information from this file

form datetime import datetime

class TrafficReportSystem:

    def __init__(self, max_reports=100):
        self.report = []
        self.max_reports = max_reports
