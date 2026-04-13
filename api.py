import cv2
from flask import Flask, Response, render_template

from analysis.traffic_analysis import TrafficAnalyzer
from src.camera_file import VehicleDetector
from src.vehicle_counter import VehicleCounter
from utils.notifier import Notifier

api = Flask(__name__)
