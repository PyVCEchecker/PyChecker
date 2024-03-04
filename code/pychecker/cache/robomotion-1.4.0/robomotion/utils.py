from pathlib import Path
from sys import platform

class File:
    @staticmethod
    def temp_dir():
        home = str(Path.home())
        is_win = platform.startswith('win')
        if is_win:
            return '%s\\AppData\\Local\\Temp\\Robomotion'%home
        return '/tmp/robomotion'

