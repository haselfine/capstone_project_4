from project_4.model.game import Game, DatabaseError

def add_game(title_in, image_url_in):
    try:
        game_obj = Game.create(title=title_in, image_url=image_url_in)
        game_obj.save()
        return 'Game saved. '
    except DatabaseError:
        return 'There was an error in adding the game.'

def find_game(title_in):
    try:
        searched_game = Game.get_or_none(Game.title == title_in)
        return searched_game
    except DatabaseError:
        return 'Sorry. There was an error retrieving the game.'

def get_all_games(game_id_in):
    try:
        return Game.select().where(Game.game_id == game_id_in)
    except DatabaseError:
        return 'Sorry. There was an error retrieving the game'

def delete_game(game_id_in):
    try:
        return Game.delete().where(Game.game_id == game_id_in).execute()
    except DatabaseError:
        return 'Sorry. There was an error deleting the artwork'