"""
Node Zuppa definer
"""
import datetime


class NodeZuppa:
    def __init__(self, str_name):
        self.name = str_name
        self.last_update = datetime.date.today()
        self.list_dtu = []  # List Directory To Update

    def add_dir(self, path):
        try:
            fp = open(path)
        except PermissionError:
            return print("\n[E] -- Error occurred trying to access the insert path\t [x_x]"
                         "[E] -- Path = " + path)
        else:
            self.list_dtu.append(fp)
