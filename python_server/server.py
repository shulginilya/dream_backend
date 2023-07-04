# Libraries imports
from flask import Flask, jsonify, request
from flask_cors import CORS

# REST app instance
app = Flask(__name__)
CORS(app)

# Sample data
sampleData = [
    {
        'id': 1,
        'title': 'Python Programming',
        'author': 'John Doe'
    },
    {
        'id': 2,
        'title': 'Flask Web Development',
        'author': 'Jane Smith'
    }
]

# TODO: establish connectionn to the DB

# Definition of REST API endpoints

# List all the data
@app.route('/', methods=['GET'])
def get_all_data():
    return jsonify(sampleData)

# List specific object
@app.route('/data/<int:id>', methods=['GET'])
def get_data_item(id):
    item = next((d for d in sampleData if d['id'] == id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Data item can not be found'}), 404

# Add a new item
@app.route('/data', methods=['POST'])
def add_data_item():
    new_data_item = request.get_json()
    sampleData.append(new_data_item)
    return jsonify({'message': 'Data item added successfully'})

# Update existed data item
@app.route('/data/<int:id>', methods=['PUT'])
def update_data_item(id):
    data_item = next((d for d in sampleData if d['id'] == id), None)
    if data_item:
        data_item.update(request.get_json())
        return jsonify({'message': 'Data item was updated successfully'})
    else:
        return jsonify({'error': 'Data item was not found'}), 404

# Delete existed item
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data_item(id):
    data_item = next((d for d in sampleData if d['id'] == id), None)
    if data_item:
        sampleData.remove(data_item)
        return jsonify({'message': 'Data item was deleted successfully'})
    else:
        return jsonify({'error': 'Data item is not found'}), 404

# Run the server
if __name__ == '__main__':
    app.run()