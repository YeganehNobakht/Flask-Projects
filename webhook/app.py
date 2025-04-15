from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    if not request.is_json:
        return jsonify({"error": "request must be json"}), 400
    data = request.get_json()
    print("Received data:", data) 
    return jsonify({"message": "Alert processed successfully"}), 200






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #Makes the server accessible on all network interfaces, not just localhost. Useful if you're running it on a server or want others on your network to connect