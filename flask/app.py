"""
Flask app for Game Viewer App
Renders and displays templates from the templates directory
Import this file and call app.start() to start web server
"""

from flask import Flask, request, render_template


app = Flask(__name__)

# TODO: Add final templates and replace all references to temp file
# TODO: get real results from IGDB API and integrate w/ Flask
sample_results = ['Halo', 'Halo 2', 'Halo 3', 'Halo: Reach', 'Halo 4', 'Halo 5', 'Halo: Infinite']
sample_image_url = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.NlLee0YLEeATwq6qh8HjjQHaLK%26pid%3DApi&f=1'

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
    # TODO: replace sample_image_url with actual image url from API
    return render_template('game.html', game_title=game_title, image_url=sample_image_url)
