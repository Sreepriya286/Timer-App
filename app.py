from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Use PORT environment variable for deployment, fallback to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

