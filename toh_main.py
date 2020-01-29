import towers_of_hanoi


def main():
    for i in range(3, 25):
        game = towers_of_hanoi.TowersOfHanoi(i)
        if i == 4:
            game.display_towers()
        game.play()
        print('Moving ', i, 'disks completed in', game.get_num_of_moves(), 'moves!')


if __name__ == '__main__':
    main()
