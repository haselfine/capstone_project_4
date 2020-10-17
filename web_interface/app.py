"""
Flask app for Game Viewer App
Renders and displays templates from the templates directory
Import this file and call app.start() to start web server
"""

from flask import Flask, request, render_template
from dataclasses import dataclass
from project_4.view.main_program import *
from project_4.view.image import *

app = Flask(__name__)
client = os.environ.get('CLIENT_ID')
api_auth = os.environ.get('AUTHORIZATION')

@dataclass
class SearchResult:
    game_title: str
    game_id: int

# starts the web server
def start():
    app.run()

@app.route('/') # GET requests
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def search_results():
    search_term = request.form["search"]
    results = search_for_game(search_term)
    #results = sample_results
    
    if results is not None and len(results) > 0:
        return render_template('home.html', list_heading='Search Results:', search_results=results)
    else:
        return render_template('home.html', list_heading='No Results Found')

@app.route('/game/<game_title>&<game_id>') # TODO: get title from request to API, not by including in url
def game(game_title, game_id):
    poster_request = call_api_covers(game_id)
    
    if poster_request[0] is not None:
        poster_url = poster_request[0]
    else:
        poster_url = None
        
    return render_template('game.html', game_title=game_title, image_url=poster_url)


def search_for_game(search_term):
    response = search_game_request(search_term)
    
    if response[0] is not None: # check if there was an error message
        results = []
        for game in response[0]:
            search_result = SearchResult(game_title=game['name'], game_id=game['id'])
            results.append(search_result)
            
        return results
    
    else:
        return None
    
