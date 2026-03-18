"""Simple Flask application with home and health endpoints."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Render the home page."""
    return render_template('index.html')


@app.route('/health')
def health():
    """Health check endpoint to verify server status."""
    return 'Server is up and running'


if __name__ == "__main__":
    app.run(port=5000)
