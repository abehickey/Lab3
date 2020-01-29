class Tower(list):
    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def get_name(self):
        return self.name

    def move(self, dest_tower):
        # Move top disk to destination tower
        dest_tower.append(self.pop())

    def __str__(self):
        tower_name = 'Tower ' + self.name + ': '
        separator = ', '
        disk_list = [str(d) for d in self]     # Loop through self list and disks to disk_list as strings.
        disk_str = separator.join(disk_list)   # Creates a string of the items in disk_list separated by ', '.
        tower_list_str = '[' + disk_str + ']'
        return tower_name + tower_list_str
