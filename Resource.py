import config
import getpass

class clsResource:
    def __init__(self):
        self.MatrixSize = config.DATABASE_CONFIG['MatrixSize']
        self.ComputerPlayer = config.DATABASE_CONFIG['ComputerPlayer']
