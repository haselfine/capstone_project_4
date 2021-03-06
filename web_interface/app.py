"""
Flask app for Game Viewer App
Renders and displays templates from the templates directory
Import this file and call app.start() to start web server
"""
from flask import Flask, request, render_template, redirect, Response
from flask_caching import Cache
from dataclasses import dataclass
from view.game_API import *
from view.image import *
from viewmodel.viewmodel import *
import datetime
import logging

cache = Cache()

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)
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
        return render_template('home.html', list_heading='No Results Found. Make sure you are authorized.')
    

@app.route('/game/<igdb_id>')
def game(igdb_id):
    
    # SQLite can only handle ints that can be stored in 64 bits
    if str.isnumeric(igdb_id) and int(igdb_id) < 2**31:
        
        game_obj = find_game_by_igdb_id(igdb_id)[0] # see if game is bookmarked

        if game_obj is None:
            bookmarked = 'false'
            game_obj = create_game_obj(igdb_id) #create game object from cached function
        else:
            bookmarked = 'true'
            
        if game_obj is not None:
            active_streamers = get_streamers(game_obj.twitch_id) #get streamers from cached function
            return render_template('game.html', game_obj=game_obj, bookmarked=bookmarked, active_streamers=active_streamers)
    
    return Response('<h1>404: Game not found</h1>', status=404)
    

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
    logging.info('Adding game to bookmark')
    logging.debug(game_data)
    
    error = add_game(game_data, False)[1]
    logging.debug(error)

    if error is None:
        return Response('status_code: 201', status=201)
    else:
        return Response('status_code: 400', status=400)


@app.route('/delete_bookmark/<game_id>', methods=['POST'])
def delete_bookmark(game_id):
    error = delete_game(game_id)[1]
    
    if error is None:
        return redirect('/bookmarks')
    else:
        return Response('status_code: 400', status=400)
    

@cache.memoize(timeout=7200) #cache search results for 2 hours (game data rarely changes)
def search_for_game(search_term):
    response = search_game_request(search_term)
    time_of_cache = datetime.datetime.now()
    logging.info(f'Cached search result at {time_of_cache}')

    if response[0] is not None: # check if there was an error message
        results = []
        for game in response[0]:
            search_result = SearchResult(game_title=game['name'], game_id=game['id'])
            results.append(search_result)
            
        return results
    
    else:
        return None  
    

@cache.memoize(timeout=3600) #game page info cached for 1 hour
def create_game_obj(igdb_id):
    game_details = get_game_info(igdb_id)[0]
    
    time_of_cache = datetime.datetime.now()
    
    if game_details is not None:
        game_obj = create_game(game_details, True)
        logging.info(f'Cached game object at {time_of_cache}')
        
        return game_obj
    
    else:
        return None


@cache.memoize(timeout=300) #current streamers cached for 5 minutes
def get_streamers(twitch_id):
    time_of_cache = datetime.datetime.now()
    logging.info(f'Cached streamers at {time_of_cache}')
    
    return get_current_streamers(twitch_id)[0]
