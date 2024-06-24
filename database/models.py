# app/models.py
from app import db
from datetime import datetime

class DroneData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drone_id = db.Column(db.String(64), index=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    location = db.Column(db.String(120), nullable=False)  # Storing as "(latitude, longitude, altitude)"
    telemetry = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return f'<DroneData {self.drone_id}>'
