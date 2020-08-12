from flask import Flask,jsonify,request,render_template


app = Flask(__name__)

stores = [{
        "name":"awesome store",
        "items":[{
            "name":"nintendo",
            'price': 15.99}]
            }]

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/store', methods=['POST']) #https://www.google.com/
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route("/store/<string:name>") #http://127.0.0.1:5000/store/some_name
def get_store(name):
    # iterate over get_stores
    for store in stores:
    # if the store name matches, return it
        if store['name'] == name:
            return jsonify(store)
    # if none match, return an error message
    return jsonify({'message': "store not found"})


@app.route("/store")
def get_stores():
    return(jsonify({'stores': stores}))

@app.route("/store/<string:name>/item", methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    # iterate over get_stores
    for store in stores:
    # if the store name matches, return it
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    # if none match, return an error message
    return jsonify({'message': "store not found"})

@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    # iterate over get_stores
    for store in stores:
    # if the store name matches, return it
        if store['name'] == name:
            return jsonify({'items':store['items']})
    # if none match, return an error message
    return jsonify({'message': "store not found"})

app.run(port=5000,debug=True)
