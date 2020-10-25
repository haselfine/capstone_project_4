from project_4.model.game import Game, DatabaseError

def add_game(title_in, image_url_in):
    try:
        game_obj = Game.create(title=title_in, image_url=image_url_in)
        game_obj.save()
        return 'Game saved.', None
    except DatabaseError:
        return None, 'There was an error in adding the game.'

def find_game(title_in):
    try:
        searched_game = Game.get_or_none(Game.title == title_in)
        return searched_game, None
    except DatabaseError:
        return None, 'Sorry. There was an error retrieving the game.'

def get_all_games():
    try:
        return Game.select(), None
    except DatabaseError:
        return None, 'Sorry. There was an error retrieving the games'

def delete_game(game_id_in):
    try:
        return Game.delete().where(Game.game_id == game_id_in).execute(), None
    except DatabaseError:
        return None, 'Sorry. There was an error deleting the artwork'
