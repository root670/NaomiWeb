import subprocess
from configparser import *
from naomigame import *

'''
A job sends a game to the NetDIMM. Each job has an accosiated process (based on tiforce_tools) that sends a game's data over the network to the NetDIMM. A transfer is started with the start() method. Status of the transfer can be checked with finished().
'''

class job:
    _game = None
    _configuration = None
    
    _game_file = None
    _process = None


    def __init__(self, naomigame, configuration):
        self._game = naomigame
        self._configuration = configuration

    def start(self):
        '''
        start the data transfer thread to send a game to the NetDIMM.

        Precondition: _game and _configuration point to valid objects. 
        Postcondition: process for loading game will be created and data will begin to be transfered to the NetDIMM.

        Return value: Always true

        '''
        print(self._configuration.items('Games'))
        game_path = self._configuration.get('Games', 'directory') + '/'+ self._game.filename
        print("Loading {}...".format(game_path))
		
        self._process = subprocess.Popen(["python3", "naomi_boot.py", game_path], shell=False)

        return True

    def finished(self):
        '''
        Return value: True if there is no process associated with the job or the associated process has ended.
        '''
        if self._process == None:
            return True
        if self._process.poll() == None:
            return False
        
        return True