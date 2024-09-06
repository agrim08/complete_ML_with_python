# Put and Delete
# Working with API's
from flask import Flask,jsonify,request

app = Flask(__name__)

#initial data:
items = [
    {'id': 1, 'name': "Item 1", 'desc': 'this is item 1'},
    {'id': 2, 'name': "Item 2", 'desc': 'this is item 2'}
]

@app.route('/')
def home():
    return 'Welcome to my project'

#GET: retrieve all items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

#GET : retrieve a specfic item by item id:
@app.route('/items/<int:item_id>',methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id),None)
    if item == None:
        return jsonify({'error':'item not found'})
    return jsonify(item)

#POST: create a new task
@app.route('/items', methods = ['POST'])
def create_item():
    #checking if the format is not in json or name is not available in item:
    if not request.json or 'name' not in request.json:
        return jsonify({'error' : 'itam not found'})
    new_item = {
        'id' : items[-1]["id"] + 1 if items else 1,
        'name' : request.json['name'],
        'desc' : request.json['desc','']
    }
    items.append(new_item)
    return jsonify(new_item)

#PUT : Update an existing item
@app.route('/items/<int:item_id>',methods = ["PUT"])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({'error' : 'item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['desc'] = request.json.get('desc',item['desc'])
    return jsonify(item)

#DELETE : Delete an item:
@app.route('/items/<int:item_id>',methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result' : "item deleted"})


if __name__ == '__main__':
    app.run(debug= True)