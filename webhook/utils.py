import os
import json
from datetime import datetime

def store_data(team_name, severity, alert_data):
    directory = f'alert/{team_name}/{severity}'
    os.makedirs(directory, exist_ok=True)
    filename = f"{directory}/alert_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(alert_data, f, indent=4)
    print(f"Alert stored at {filename}")