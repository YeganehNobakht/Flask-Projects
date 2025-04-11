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


@app.route("/get-all/<format>", methods=["GET"])
def get_all_note(format):
    # Read the notes data from the JSON file
    notes = utils.read_json("note_data.json")

    

    if format in ["yml", "yaml"]:
        # Convert the notes to YAML format and return it as plain text
        yaml_data = utils.convert_json_to_yml(notes)
        return app.response_class(yaml_data, content_type='application/x-yaml')
    else :
        # Return notes in JSON format
        return jsonify(notes)

    return jsonify({'error': 'Unsupported format'}), 200

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


@app.route('/delete-note/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    notes = utils.read_json("note_data.json")

    # Use filter to exclude the note with the matching ID
    updated_notes = list(filter(lambda note: note.get('id') != note_id, notes))

    if len(updated_notes) == len(notes):
        return jsonify({'error': 'Note not found.'}), 200

    utils.write_json_to_file(updated_notes, "note_data.json")
    return jsonify({'message': f'Note {note_id} deleted successfully.'})


@app.route("/update-note", methods=['PUT'])
def update_note():
    data = request.get_json()

    notes = utils.read_json("note_data.json")

    allowed_fields = ['id', 'title', 'content', 'timestamp']

    # Check for extra fields in the data
    extra_fields = [field for field in data if field not in allowed_fields]
    if extra_fields:
        return jsonify({'error': f'Invalid fields: {", ".join(extra_fields)}'}), 400

    # Find the note with the matching ID and update it
    for i, note in enumerate(notes):
        if note.get('id') == data.get("id"):
            notes[i] = {**note, **data}  # Merge and update the note
            utils.write_json_to_file(notes, "note_data.json")
            return jsonify({'message': f'Note {data["id"]} updated successfully.'})

    return jsonify({'error': 'Note not found.'}), 200


if __name__ == "__main__":
    app.run(debug=True)
