from flask import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
	

    
@app.route('/<path:path>')
def index_css_8(path):
    return send_from_directory('templates', path)
	