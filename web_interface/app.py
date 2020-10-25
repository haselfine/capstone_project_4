"""
Flask app for Game Viewer App
Renders and displays templates from the templates directory
Import this file and call app.start() to start web server
"""

from flask import Flask, request, render_template, redirect
from dataclasses import dataclass
from project_4.view.main_program import *
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
    

@app.route('/game/<game_title>&<game_id>') # TODO: get title from request to API, not by including in url
def game(game_title, game_id):
    bookmark = find_game(game_title)[0] # see if game is bookmarked

    if bookmark is None:
        bookmarked = 'false'
        poster_request = call_api_covers(game_id)
    else:
        bookmarked = 'true'
        poster_request = bookmark.image_url, None
    
    if poster_request[0] is not None:
        image_url = poster_request[0]
    else:
        image_url = None
        
    return render_template('game.html', game_title=game_title, image_url=image_url, bookmarked=bookmarked)


@app.route('/bookmarks')
def bookmarks():
    bookmarked_games = get_all_games()[0]
    
    if bookmarked_games is not None and len(bookmarked_games) > 0:
        return render_template('bookmarks.html', list_heading='All Bookmarks:', bookmarks=bookmarked_games)
    else:
        return render_template('bookmarks.html', list_heading='No Bookmarks (yet!)')


@app.route('/bookmarked_game/<game_title>')
def bookmarked_game(game_title):
    game = find_game(game_title)[0]
    
    if game is not None:
        return render_template('game.html', game_title=game.title, image_url=game.image_url, bookmarked='true')
    else:
        # redirect to home page if not found
        redirect('/')
        

@app.route('/add_bookmark', methods=['POST'])
def add_bookmark():
    game_title = request.form['game_title']
    image_url = request.form['image_url']
    
    error = add_game(game_title, image_url)[1]
    
    if error is None:
        return '{\'status\': 200}'
    else:
        return '{\'status\': 400, \'message\': {error}}'


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
    
