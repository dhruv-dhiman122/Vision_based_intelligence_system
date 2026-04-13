import cv2
from flask import Flask, Response, render_template

from analysis.traffic_analysis import TrafficAnalyzer
from main import analyzer, detector
from src.camera_file import VehicleDetector
from src.vehicle_counter import VehicleCounter
from utils.notifier import Notifier

api = Flask(__name__)

# init module
detector = VehicleDetector()
counter = VehicleCounter(line_position=300)
analyzer = TrafficAnalyzer()

notifier = Notifier("YOUR_TOKEN", "CHAT_ID")

cap = cv2.VideoCapture("video2.mp4")

frame_count = 0
