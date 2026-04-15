# This file is made for driver to help each other on based of the traffic level
# IDEA TODO -> make the chatbot take more information from this file

from datetime import datetime


class TrafficReportSystem:
    def __init__(self, max_reports=100):
        self.reports = []
        self.max_reports = max_reports

    def add_report(self, location: str, message: str):
        report = {
            "location": location,
            "message": message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.reports.append(report)

        # keep list size controller
        if len(self.reports) > self.max_reports:
            self.reports.pop(0)

        return report

    def get_reports(self):
        return self.reports

    def get_recent_reports(self, limit=5):
        return self.reports[-limit:]

    def get_reports_by_location(self, location: str):
        return [r for r in self.reports if r["location"].lower() == location.lower()]
