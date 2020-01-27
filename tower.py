class Tower(list):
    def __init__(self, name):
        list.__init__(self, name):
            self.name = name

    def get_name(self):
        return self.name

    def move(self):
