from flask import Flask
from time import sleep
#app = Flask("moshe")
#@app.route('/')

#def hello_world():
  # text = 'Investiogation Center <br> ic_admin <br> ic_admin'
 #  return text

#app.run(host='0.0.0.0', port="8080")

from flask import Flask, jsonify, request
app = Flask("moshe")
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({"message": "Item deleted successfully"})

app.run(host='0.0.0.0',port="8082")

app.run