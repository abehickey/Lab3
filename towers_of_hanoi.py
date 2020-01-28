import tower
import disk


class TowersOfHanoi:
    def __init__(self, num_disks):
        self.num_of_disks = num_disks
        self.num_of_moves = 0
        # self.A = tower.Tower('A')
        # self.B = tower.Tower('B')
        # self.C = tower.Tower('C')
        self.towers = [self.tower.Tower('A'), self.tower.Tower('B'), self.tower.Tower('C')]
        for i in range(num_disks, 0, -1):
            self.towers[0].append(disk.Disk(i))

    def get_num_of_moves(self):
        return self.num_of_moves

    def move_disks(self, num_disks_to_move, source, helper, target):
        n = num_disks_to_move
        if n == 1:
            # The following code is performed in the
            # Tower move method in your Tower class
            target.append(source.pop())
            # Display the towers here
            # Increment the count of moves at this location
            self.num_of_moves += 1
        else:
            # move tower of size n-1 to helper:
            self.move_disks(n - 1, source, target, helper)
            # move largest disk from source peg to target peg
            self.move_disks(1, source, helper, target)
            # move tower of size n-1 from helper to target
            self.move_disks(n - 1, helper, source, target)

    def play(self):
        self.move_disks(len(self.towers[0]), self.towers[0], self.towers[1], self.towers[2])

    def display_towers(self):
        pass
