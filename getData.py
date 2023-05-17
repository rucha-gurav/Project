import requests
import time

# Datadog API credentials
API_KEY = 'YOUR_API_KEY'
APP_KEY = 'YOUR_APP_KEY'

# Monitor ID for which you want to fetch alert details
MONITOR_ID = 'YOUR_MONITOR_ID'

# Datadog API endpoints
MONITOR_ENDPOINT = f"https://api.datadoghq.com/api/v1/monitor/{MONITOR_ID}"
ALERTS_ENDPOINT = f"https://api.datadoghq.com/api/v1/monitor/{MONITOR_ID}/all"

# Datadog API request headers
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': API_KEY,
    'DD-APPLICATION-KEY': APP_KEY
}

# Get monitor details
monitor_response = requests.get(MONITOR_ENDPOINT, headers=headers)
monitor_data = monitor_response.json()

# Get all alerts for the monitor
alerts_response = requests.get(ALERTS_ENDPOINT, headers=headers)
alerts_data = alerts_response.json()

# Extract alert triggered time and recovered time (if available)
for alert in alerts_data:
    if alert['alert_type'] == 'triggered':
        triggered_time = time.ctime(alert['date_triggered'])
        print("Alert Triggered Time:", triggered_time)
    elif alert['alert_type'] == 'recovered':
        recovered_time = time.ctime(alert['date_triggered'])
        print("Alert Recovered Time:", recovered_time)
