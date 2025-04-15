from flask import Flask, request, jsonify
import emailer
import utils

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    if not request.is_json:
        return jsonify({"error": "request must be json"}), 400
    data = request.get_json()

    alerts = data.get("alerts")
    for alert in alerts:
        try:
            team = alert.get("labels", {}).get("team", "unknown_team")
            severity = alert.get("labels", {}).get("severity", "unknown_severity")
            summary = alert.get("annotations", {}).get("summary", "No summary")
            description = alert.get("annotations", {}).get("description", "No description")

            # 1. Store to file
            utils.store_data(team, severity, alert)

            # 2. Send email notification
            emailer.send_email_alert(summary, description)

        except Exception as e:
            print(f"Error handling alert: {e}")
            continue

        return jsonify({"message": "Alerts processed"}), 200






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #Makes the server accessible on all network interfaces, not just localhost. Useful if you're running it on a server or want others on your network to connect