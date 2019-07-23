import  datetime
import time
import config
import getpass
from datetime import date

class clsResource:
    def __init__(self):
        self.MatrixSize = config.DATABASE_CONFIG['MatrixSize']
        self.ComputerPlayer = config.DATABASE_CONFIG['ComputerPlayer']
