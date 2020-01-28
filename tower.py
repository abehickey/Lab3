class Tower(list):
    def __init__(self, name):
        super().__init__(self, name)
        self.name = name

    def get_name(self):
        return self.name

    def move(self, dest_tower):
        pass

    def __str__(self):
        tower_name = 'Tower ' + self.name + ': '
        separator = ', '
        disk_list = [str(d) for d in self]   #Comment what line is doing
        disk_str = separator.join(disk_list) #Comment what line is doing
        tower_list_str = '[' + disk_str + ']'
        return tower_name + tower_list_str
