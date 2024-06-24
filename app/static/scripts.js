// app/static/scripts.js

document.addEventListener('DOMContentLoaded', (event) => {
    var map = L.map('map').setView([51.505, -0.09], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    drones.forEach(function(drone) {
        var location = drone.location.replace(/[()]/g, '').split(', ');
        var latitude = parseFloat(location[0]);
        var longitude = parseFloat(location[1]);
        L.marker([latitude, longitude]).addTo(map)
            .bindPopup('<b>Drone ID:</b> ' + drone.drone_id + '<br><b>Timestamp:</b> ' + drone.timestamp + '<br><b>Telemetry:</b> ' + drone.telemetry);
    });
});
