from naomigame import *

'''
A job sends a game to the NetDIMM. Each job has an accosiated thread that sends a game's data over the network to the NetDIMM. A transfer is started with the start() method. The status of the transfer can be checked with the progress() and finished() methods.
'''

class job:
	_game = None
	_configuration = None
	
	_game_file = None
	_thread = None


	def __init__(self, naomigame, configuration):
		_current_game = naomigame
		_configuration = configuration

		return true

	def start(self):
		'''
		start the data transfer thread to send a game to the NetDIMM.

		Precondition: _game and _configuration point to valid objects. 
		Postcondition: thread for loading game will be created and data will begin to be transfered to the NetDIMM.

		Return value: True if _game_file (who's filename is _current_game.filename) was opened without error and the loading thread was successfully started. False if gamefile couldn't be opened

		open _game_file
		start loading thread
		return true if nothing went wrong
		otherwise return false


		'''

		return true

	def progress(self):
		'''
		Return value: percentage of data in _game_file that has been sent to the NetDIMM

		get bytes sent from loading thread

		return (bytes sent)/_game.size * 100
		'''
		return true

	def finished(self):
		'''
		Return value: True if all data in _game_file has been sent to the NetDIMM. False if more data needs to be sent.
		'''
		return false