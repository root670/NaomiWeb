from bottle import route, run, template, static_file, error, request, view
import os
import string
import configparser
from naomigame import *
from loadgame import *

PREFS_FILE = "settings.cfg"
prefs = configparser.ConfigParser()
            
def build_games_list():
    games = []
    games_directory = prefs['Games']['directory'] or 'games'
    
    print("Looking for NAOMI games...")
    
    if os.path.isdir(games_directory):
        for filename in os.listdir(games_directory):
            filename = games_directory + '/' + filename
            print(filename)
            if(is_naomi_game(filename)):
                game = NAOMIGame(get_game_name(filename), filename)
                games.append(game)
                
        return games
        
    else:
        return None

@route('/')
def index():
    some_games = build_games_list()
    if some_games != None:
        return template('index', games=some_games)
    else:
        return template('index')
        

@route('/load/<hashid:int>')
def load(hashid):
    some_games = build_games_list()
    for game in some_games:
        if game.__hash__() == hashid:
            return "Found the game" + str(hashid) + ", creating job..."

    return "Unable to find" + str(hashid) + '!'

@route('/config', method='GET')
def config():
    network_ip = prefs['Network']['ip'] or '192.168.0.10'
    network_subnet = prefs['Network']['subnet'] or '255.255.255.0'
    games_directory = prefs['Games']['directory'] or 'games'
    
    return template('config', network_ip=network_ip, network_subnet=network_subnet, games_directory=games_directory)

@route('/config', method='POST')
def do_config():
    network_ip = request.forms.get('network_ip')
    network_subnet = request.forms.get('network_subnet')
    games_directory = request.forms.get('games_directory')
    
    prefs['Network']['ip'] = network_ip
    prefs['Network']['subnet'] = network_subnet
    prefs['Games']['directory'] = games_directory
    with open(PREFS_FILE, 'w') as prefs_file:
        prefs.write(prefs_file)

    return template('config', network_ip=network_ip, network_subnet=network_subnet, games_directory=games_directory, did_config=True)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, 'static')

@error(404)
def error404(error):
    return '<p>Error: 404</p>'

prefs_file = open(PREFS_FILE, 'r')
prefs.read_file(prefs_file)
prefs_file.close()

run(host='0.0.0.0', port=8000, debug=True)