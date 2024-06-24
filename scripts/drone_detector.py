# scripts/drone_detector.py
import rtl_sdr
import opendroneid
from datetime import datetime
import sqlite3

def detect_drones():
    # Initialize SDR
    sdr = rtl_sdr.RtlSdr()
    
    # Configure SDR
    sdr.sample_rate = 2.048e6
    sdr.center_freq = 2.4e9
    sdr.gain = 'auto'
    
    while True:
        samples = sdr.read_samples(256*1024)
        messages = opendroneid.decode(samples)
        for message in messages:
            process_drone_data(message)

def process_drone_data(message):
    drone_id = message.basic_id
    timestamp = datetime.now()
    location = (message.location.latitude, message.location.longitude, message.location.altitude)
    telemetry = {
        'direction': message.location.direction,
        'speed': message.location.speed,
        'authentication': message.authentication,
        'self_id': message.self_id,
        'system': message.system,
        'operator_id': message.operator_id
    }

    # Save data to the database
    save_to_database(drone_id, timestamp, location, telemetry)

def save_to_database(drone_id, timestamp, location, telemetry):
    conn = sqlite3.connect('/path/to/your/database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO DroneData (drone_id, timestamp, location, telemetry)
                      VALUES (?, ?, ?, ?)''', (drone_id, timestamp, str(location), str(telemetry)))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    detect_drones()
