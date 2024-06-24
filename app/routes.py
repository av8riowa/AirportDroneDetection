# app/routes.py
from flask import Blueprint, render_template
from app.models import DroneData

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    drones = DroneData.query.all()
    return render_template('index.html', drones=drones)

@bp.route('/drone/<int:id>')
def drone_details(id):
    drone = DroneData.query.get_or_404(id)
    return render_template('drone_details.html', drone=drone)

@bp.route('/history')
def history():
    return render_template('history.html')

@bp.route('/reports')
def reports():
    return render_template('reports.html')
