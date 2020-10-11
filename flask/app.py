"""
Flask app for Steam/Twitch Connector
Renders and displays templates from the templates directory
Import this file and call app.start() to start web server
"""

from flask import Flask, request, render_template


app = Flask(__name__)

"""
TODO: Add final templates and replace all references to temp file
"""

# starts the web server
def start():
    app.run()

@app.route('/')
def home():
    return render_template('temp.html', final_page_name='home.html')
