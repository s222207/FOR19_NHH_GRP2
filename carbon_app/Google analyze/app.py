from flask import Flask, request, jsonify, render_template
import requests
from flask_uploads import UploadSet, configure_uploads
import json

app = Flask(__name__)

app.config['UPLOADED_FILES_DEST'] = 'uploads'
app.config['UPLOADS_DEFAULT_DEST'] = 'uploads/'
app.config['UPLOADS_DEFAULT_URL'] = '/uploads/'

uploaded_files = UploadSet('files', extensions=('json',))
configure_uploads(app, uploaded_files)

CARBON_INTERFACE_API_KEY = 'x8biWMp1oCOylyZiGtZMxg	'

def convert_activity_type_to_transport_method(activity_type):
    conversion_map = {
        'WALKING': 'walking',
        'CYCLING': 'cycling',
        'IN_PASSENGER_VEHICLE': 'car',
        'IN_BUS': 'bus',
        'IN_TRAIN': 'train',
        'IN_SUBWAY': 'subway',
        'IN_TRAM': 'tram',
        'IN_FERRY': 'ferry',
        'FLYING': 'plane',
        'MOTORCYCLING': 'motorbike',
    }
    return conversion_map.get(activity_type)

@app.route('/')
def index():
    return render_template('index.html')

def calculate_emissions(transportation_method, distance_meters):
    headers = {
        "Authorization": f"Bearer {CARBON_INTERFACE_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "type": "transportation",
        "transportation_method": transportation_method,
        "distance_unit": "km",
        "distance_value": distance_meters / 1000,
    }
    response = requests.post("https://www.carboninterface.com/api/v1/estimates", headers=headers, json=data)

    if response.status_code == 200:
        emissions = response.json()["data"]["attributes"]["carbon_kg"]
        return emissions
    else:
        print("Error: Unable to calculate emissions. Status code:", response.status_code)
        return None
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'file' in request.files:
        filename = uploaded_files.save(request.files['file'])
        activities_summary = analyze_activities(filename)
        return render_template('results.html', activities_summary=activities_summary,)
    return render_template('upload.html')

EMISSION_FACTORS = {
    'walking': 0,
    'cycling': 0,
    'car': 0.12,  # kg CO2 per km
    'bus': 0.08,  # kg CO2 per km
    'train': 0.04,  # kg CO2 per km
    'subway': 0.05,  # kg CO2 per km
    'tram': 0.03,  # kg CO2 per km
    'ferry': 0.3,  # kg CO2 per km
    'plane': 0.25,  # kg CO2 per km
    'motorbike': 0.1,  # kg CO2 per km
}

from collections import defaultdict

def analyze_activities(filename):
    with open('uploads/' + filename) as f:
        data = json.load(f)

    activities_summary = defaultdict(lambda: {'distance': 0, 'emissions': 0})

    for item in data['timelineObjects']:
        if 'activitySegment' in item:
            activity = item['activitySegment']
            activity_type = activity['activityType']
            distance_meters = activity.get('distance', 0)

            transport_method = convert_activity_type_to_transport_method(activity_type)
            if transport_method:
                distance_km = distance_meters / 1000
                activities_summary[transport_method]['distance'] += distance_km
                activities_summary[transport_method]['emissions'] += distance_km * EMISSION_FACTORS[transport_method]

    return activities_summary



if __name__ == '__main__':
    app.run(debug=True)
