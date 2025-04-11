from flask import Flask, request, jsonify
from datetime import datetime
import utils
import uuid

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome"


@app.route("/status")
def status():
    return "Server is running"


@app.route("/about")
def about():
    return "This is a simple note-taking web app built with Flask"


@app.route("/ping", methods=["GET"])
def ping():
    return "pong"


@app.route("/create-note", methods=["POST"])
def create_note():
    required_fields = ['title', 'content']
    data = request.get_json()

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({'error': f'Missing fields: {", ".join(missing_fields)}'}), 400

    # Add current timestamp and Id
    data['id'] = str(uuid.uuid4())
    data["timestamp"] = datetime.now().isoformat()

    # Read existing notes and append the new one
    note_data = utils.read_json("note_data.json")
    note_data.append(data)

    # Write back to file
    utils.write_json_to_file(note_data, "note_data.json")

    # Return the newly added note
    return jsonify(data)


@app.route('/get-note/<note_id>', methods=['GET'])
def get_note(note_id):
    notes = utils.read_json("note_data.json")
    
    for note in notes:
        if note.get('id') == note_id:
            return jsonify(note)

    return jsonify({'error': 'Note not found.'}), 200

if __name__ == "__main__":
    app.run(debug=True)
