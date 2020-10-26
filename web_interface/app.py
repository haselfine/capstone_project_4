"""
Flask app for Game Viewer App
Renders and displays templates from the templates directory
Import this file and call app.start() to start web server
"""

from flask import Flask, request, render_template, redirect
from dataclasses import dataclass
from project_4.view.game_API import *
from project_4.view.image import *
from project_4.viewmodel.viewmodel import *

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
    
    if results is not None and len(results) > 0:
        return render_template('home.html', search_term=search_term, list_heading='Search Results:', search_results=results)
    else:
        return render_template('home.html', list_heading='No Results Found')
    

@app.route('/game/<game_id>')
def game(game_id):
    game_obj = find_game_by_igdb_id(game_id)[0] # see if game is bookmarked

    if game_obj is None:
        bookmarked = 'false'
        game_details = get_game_info(game_id)[0]
        
        if game_details is not None:
            game_obj = create_game(game_details, True)
    else:
        bookmarked = 'true'
        
    return render_template('game.html', game_obj=game_obj, bookmarked=bookmarked)


@app.route('/bookmarks')
def bookmarks():
    bookmarked_games = get_all_games()[0]
    
    if bookmarked_games is not None and len(bookmarked_games) > 0:
        return render_template('bookmarks.html', list_heading='All Bookmarks:', bookmarks=bookmarked_games)
    else:
        return render_template('bookmarks.html', list_heading='No Bookmarks (yet!)')
        

@app.route('/add_bookmark', methods=['POST'])
def add_bookmark():
    game_data = request.form.to_dict(True)
    
    error = add_game(game_data, False)[1]
    
    if error is None:
        return '200'
    else:
        return '400'


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
