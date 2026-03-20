import os
from flask import Flask, request, jsonify, render_template
from search import search_clothing

# Get the frontend folder path
frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')

app = Flask(__name__, 
            template_folder=frontend_path,
            static_folder=frontend_path,
            static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    dimensions = data.get('dimensions')
    description = data.get('description')
    
    if not dimensions or not description:
        return jsonify({'error': 'Dimensions and description are required'}), 400
    
    results = search_clothing(dimensions, description)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)