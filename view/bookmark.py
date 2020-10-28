from viewmodel.viewmodel import add_game, get_all_games, delete_game, find_game

def bookmark_game(game_title, game_url):
    while True:
        user_choice = input(f'Would you like to save {game_title} to your bookmarks? y or n')
        if user_choice.lower() == 'y':
            return add_game(game_title, game_url)
        elif user_choice.lower() == 'n':
            return 'Game was not added.'
        else:
            print('You must respond either y or n')

def retrieve_bookmarks():
    return get_all_games()

def find_bookmark_by_title(title):
    return find_game(title)

def delete_bookmark(title):
    bookmark_id = find_bookmark_by_title(title).game_id
    while True:
        user_choice = input(f'Are you sure you would like to delete {title} from your bookmarks? y or n')
        if user_choice.lower() == 'y':
            return delete_game(bookmark_id)
        elif user_choice.lower() == 'n':
            return 'Bookmark was not deleted'
        else:
            print('You must respond either y or n')
