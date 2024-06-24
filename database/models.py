# database/models.py
from app import db
from datetime import datetime

class DroneData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drone_id = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(120))
    telemetry = db.Column(db.String(120))

    def __repr__(self):
        return f'<DroneData {self.drone_id}>'
