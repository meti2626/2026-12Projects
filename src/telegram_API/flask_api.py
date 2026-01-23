from flask import Flask, jsonify, request

# Create the Flask app instance
app = Flask(__name__)

# Define a root route
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello from Flask! This is another API example.'})

# Define a dynamic route
@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = {
        'id': user_id,
        'name': f'User {user_id}',
        'status': 'active'
    }
    return jsonify(user_data)

# Define a POST route to receive data
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
        
    return jsonify({
        'message': 'Data received successfully',
        'received_data': data
    }), 201

if __name__ == '__main__':
    # Run the Flask app
    # debug=True allows the server to reload on code changes
    app.run(debug=True, port=5000)
