import sys
import os

# Get the parent directory of the current file (launcher.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add parent directory to the Python path
sys.path.insert(0, parent_dir)

from src.data_preprocessing.process_input import process_input
from flask import Flask, render_template, request

#export to HTML
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # Get form data
        # Addresses
        address1 = str(request.form['address1'])
        address2 = str(request.form['address2'])
        address3 = str(request.form['address3'])
        address4 = str(request.form['address4'])

        # Path parameters
        color = str(request.form['color'])
        weight = str(request.form['weight'])

        # Map parameters
        zoom = str(request.form['zoom'])
        size = str(request.form['size'])
        maptype = str(request.form['maptype'])

        # Process input by calling the function
        image_url = process_input(address1, address2, address3, address4, color, weight, zoom, size, maptype)

        # Render a template with the processed datax
        return render_template('index.html', image_url=image_url)
    
if __name__ == '__main__':
    app.run(debug=True, port=5500)

