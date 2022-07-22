import random

class Game():
    def __init__(self):
        self.items = ['r', 'p', 's']

    def get_user_item(self):
        item = ''
        while item not in self.items:
            item = input('Select (r)ock, (p)aper or (s)cissors: ').lower()
        return item

    def get_computer_item(self):
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        if user_item == 'r' and computer_item == 's':
            return 'win'
        elif user_item == 'p' and computer_item == 'r':
            return 'win'
        elif user_item == 's' and computer_item == 'p':
            return 'win'
        elif user_item == computer_item:
            return 'draw'
        else:
            return 'loss'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_result = self.get_game_result(user_item, computer_item)
        print(f'You choose: {user_item}\nComputer chose: {computer_item}\nResult: {game_result}')
        return game_result

def get_user_menu_choice():
    print('\nMenu:\n(P)lay a new game\n(S)how scores\n(Q)uit')
    menu_option = input('Select menu option: ').lower()
    return menu_option


def print_results(results):
    print(f'Game Results:\nWin: {results["win"]}\nLoss: {results["loss"]}\nDraw: {results["draw"]}\nThank you for playing!')


def main():
    menu_choice = ''
    scores = {'win': 0, 'loss': 0, 'draw': 0}

    while menu_choice != 'q':
        menu_choice = get_user_menu_choice()

        if menu_choice == 'p':
            new_game = Game()
            game_result = new_game.play()
            scores[game_result] += 1
        elif menu_choice == 's':
            print_results(scores)
        else:
            print_results(scores)
            print('Goodbye!')
            break


main()
