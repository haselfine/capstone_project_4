"""
Flask app for Game Viewer App
Renders and displays templates from the templates directory
Import this file and call app.start() to start web server
"""

from flask import Flask, request, render_template


app = Flask(__name__)

# TODO: Add final templates and replace all references to temp file
# TODO: get real results from IGDB API
sample_results = ['Halo', 'Halo 2', 'Halo 3', 'Halo: Reach', 'Halo 4', 'Halo 5', 'Halo: Infinite']

# starts the web server
def start():
    app.run()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def search_results():
    return render_template('home.html', list_heading='Search Results:', search_results=sample_results)

@app.route('/game/<game_title>')
def game(game_title):
    return render_template('temp.html', final_page_name=f'{game_title} Details Page')
