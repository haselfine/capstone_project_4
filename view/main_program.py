from project_4.viewmodel import *

def main():
    get_input_from_user()
    #TODO connect to APIs
    #TODO search games in Steam, Twitch.tv
    #TODO store game info
    pass





def  get_input_from_user():
    title_in = ui.get_string('Enter game title')
    try:
        viewmodel.find_game(title_in)
    except:
        print ('not found this game ')
    


if __name__ == '__main__':
    main()