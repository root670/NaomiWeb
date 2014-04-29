import io
import os

class NAOMIGame(object):
    name = ""
    filename = ""
    size = 0
    
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename
        try:
            self.size = os.stat(filename).st_size
        except Exception:
            self.size = 0
    
    def __hash__(self):
        return hash((self.name, self.filename, self.size)) & 0xffffffff

def is_naomi_game(filename):
    'Determine (loosely) if a file is a valid NAOMI netboot game'
    try:
        fp = open(filename, 'rb')
        header_magic = fp.read(5).decode('utf-8')
        fp.close()
        return header_magic == 'NAOMI'

    except Exception:
        print("is_naomi_game(): Could not open " + filename)
        return False

def get_game_name(filename):
    'Read game name from NAOMI rom file.'
    try:
        fp = open(filename, 'rb')
        fp.seek(0x30, os.SEEK_SET)
        filename = fp.read(32).decode('utf-8').rstrip(' ')
        fp.close()
        return filename

    except Exception:
        print("get_game_name(): Error reading game name.")
        return ''