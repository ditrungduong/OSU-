# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 11/19/2022
# Description: write a class called Mancala that allows two people to play a text-based version of the game

class Player:
    """Represent player"""

    def __init__(self, name, player_num, player_board):
        self._player_name = name
        self._player_num = player_num
        self._player_board = player_board
        self._player_game_board_seq = {'1': '2', '2': '3', '3': '4', '4': '5', '5': '6',
                                       '6': 'store_1', 'store_1': '7', '7': '8', '8': '9',
                                       '9': '10', '10': '11', '11': '12', '12': 'store_2',
                                       'store_2': '1'}
        self._player_opposite_pit = {'1': '12', '2': '11', '3': '10', '4': '9', '5': '8', '6': '7',
                                     '12': '1', '11': '2', '10': '3', '9': '4', '8': '5', '7': '6'}

    def __str__(self):
        """Return string value instead of memory location"""
        return str(self._player_name) + " " + str(self._player_num)

    def get_opposite_pit(self):
        """Return opposite board"""
        return self._player_opposite_pit

    def set_player_board(self, board_number):
        """Assigning player board according to their number"""
        self._player_board = board_number

    def get_player_board(self):
        """Return player board map"""
        return self._player_board

    def get_player_name(self):
        """Return player name"""
        return self._player_name

    def get_player_num(self):
        """"Return player number"""
        return self._player_num

    def get_player_store(self, num):
        """Return player store"""
        return self.get_player_board()[('store_' + str(num))]

    def get_game_board_seq(self):
        """Return game board sequence"""
        return self._player_game_board_seq


class Board:
    def __init__(self):
        self._opposite_board = {'1': '12', '2': '11', '3': '10', '4': '9', '5': '8', '6': '7',
                                '12': '1', '11': '2', '10': '3', '9': '4', '8': '5', '7': '6'}
        self._game_board_sequence = {'1': '2', '2': '3', '3': '4', '4': '5', '5': '6',
                                     '6': '7', '7': 'store_1', 'store_1': '8', '8': '9',
                                     '9': '10', '10': '11', '11': '12', '12': 'store_2',
                                     'store_2': '1'}

        self._player_1_board = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, 'store_1': 0}
        self._player_2_board = {'7': 4, '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, 'store_2': 0}

    def get_board_map(self, player_num):
        """Return player board base on player number input"""
        if player_num == 1:
            return self._player_1_board
        return self._player_2_board


class Mancala:
    """Represent Mancala game class"""

    def __init__(self):
        self._player_list = {}
        self._current_turn = None
        self._game_board = Board()
        self._game_board_score = []

    def create_player(self, new_player_name):
        """Creating new player and add to the player list"""
        # if player list already has value - player 1 already exist - player 2 will be created
        if self._player_list:
            # Assigning player 2 : Player 2 attribute with name, player number, player board, and opponent board)
            self._player_list[2] = Player(new_player_name, 2, self._game_board.get_board_map(2))
            # Assigning player 1 attributes
        else:
            self._player_list[1] = Player(new_player_name, 1, self._game_board.get_board_map(1))

    def player_move(self, player_turn, pit_number):
        """Making move base on player turn and pit choice"""
        # Get value of seeds from the pit number
        seed_to_go = self._player_list[player_turn].get_player_board()[str(pit_number)]
        self._player_list[player_turn].get_player_board()[str(pit_number)] = 0  # Set seed amount to 0 after take out
        while seed_to_go > 0:  # Continue placing seed until empty
            pit_number = self._player_list[player_turn].get_game_board_seq()[str(pit_number)]  # Move to next pit
            if (player_turn == 1 and pit_number == 'store_2') or (
                    player_turn == 2 and pit_number == 'store_1'):
                continue  # Skip opponent store
            if player_turn == 1 and pit_number == 'store_1':  # adding seed to store 1
                self._player_list[player_turn].get_player_board()['store_1'] += 1
            elif player_turn == 2 and pit_number == 'store_2':  # adding seed to store 2
                self._player_list[player_turn].get_player_board()['store_2'] += 1
            else:
                # Adding seed to each pit
                if 1 <= int(pit_number) <= 6 or pit_number == 'store_1':
                    self._player_list[1].get_player_board()[str(pit_number)] += 1
                else:
                    self._player_list[2].get_player_board()[str(pit_number)] += 1
            seed_to_go -= 1  # Removing seed after placing

        # Check if last placing seed was in an empty pit, gain opposite pit's seeds.
        # If last placing seed was in store 1 or store 2. Skip
        if pit_number == 'store_1' or pit_number == 'store_2':
            None
        # If player 1 place the last seed in a previously empty pit.
        elif player_turn == 1 and str(pit_number) in self._player_list[player_turn].get_player_board() and \
                self._player_list[player_turn].get_player_board()[str(pit_number)] == 1:
            # Find the opposite pit by using opposite pit map
            opposite_pit = self._player_list[player_turn].get_opposite_pit()[str(pit_number)]
            # Getting opposite pit value
            opposite_pit_value = self._player_list[2].get_player_board()[opposite_pit]
            # Taking value from opposite pit and add to store 1
            self._player_list[player_turn].get_player_board()['store_1'] += opposite_pit_value + 1
            # Empty out the opponent pit
            self._player_list[2].get_player_board()[str(opposite_pit)] = 0
            # Empty out the current pit
            self._player_list[player_turn].get_player_board()[str(pit_number)] -= 1
        # The same logic apply for player 2
        elif player_turn == 2 and str(pit_number) in self._player_list[player_turn].get_player_board() and \
                self._player_list[player_turn].get_player_board()[str(pit_number)] == 1:
            opposite_pit = self._player_list[player_turn].get_opposite_pit()[str(pit_number)]
            opposite_pit_value = self._player_list[1].get_player_board()[opposite_pit]
            self._player_list[player_turn].get_player_board()['store_2'] += opposite_pit_value + 1
            self._player_list[1].get_player_board()[str(opposite_pit)] = 0
            self._player_list[player_turn].get_player_board()[str(pit_number)] -= 1

        # Checking if the last send landed in the player store, if yes then take another turn
        if (pit_number == 'store_1' and player_turn == 1) or (pit_number == 'store_2' and player_turn == 2):
            print(f"player {player_turn} take another turn")
            # Keep the game turn the same as current player turn
            self._current_turn = player_turn
        else:
            # Rotating player turn if last pit landed in other case
            if player_turn == 1:
                # If current player turn is 1 then change it to 2
                self._current_turn = 2
                return
            elif player_turn == 2:
                self._current_turn = 1
                return

    def check_end_game(self):
        """Return True if the game has come to an end """
        player_1_score = int()
        player_2_score = int()
        # Looping through player 1 score
        for num in range(1, 7):
            player_1_score += self._player_list[1].get_player_board()[str(num)]
        # Looping through player 2 score
        for num in range(7, 13):
            player_2_score += self._player_list[2].get_player_board()[str(num)]
        # If one of the player pit has emptied out all pit. Game end.
        if player_1_score == 0 or player_2_score == 0:
            self._game_board_score.clear()
            # Iterate through the dict of player board to get back just the values of each pit
            player_1_score += self._player_list[1].get_player_board()['store_1']
            player_2_score += self._player_list[2].get_player_board()['store_2']
            self._player_list[2].get_player_board()['store_2'] = player_2_score
            self._player_list[1].get_player_board()['store_1'] = player_1_score

            for num in range(1, 7):
                # Setting value of all pit  zero since it the game is done
                player_1_score += self._player_list[1].get_player_board()[str(num)]
                self._player_list[1].get_player_board()[str(num)] = 0
                # Adding value to the game board score
            for value in self._player_list[1].get_player_board().values():
                # Adding value to the game board score
                self._game_board_score.append(value)
            for num in range(7, 13):
                player_2_score += self._player_list[2].get_player_board()[str(num)]
                self._player_list[2].get_player_board()[str(num)] = 0
                # Adding value to the game board score
            for value in self._player_list[2].get_player_board().values():
                self._game_board_score.append(value)
            return "Game is ended"


    def play_game(self, player_turn, pit_choice):
        """Start game, passing players number and turns pit choice, add participating player to player_list dictionary,
        iterate through turns list to move tokens, return a list of seed amount for each of the pit.
        """
        if 6 < pit_choice or pit_choice < 1:
            return "Invalid number for pit index"
        if player_turn == 2:
            pit_choice = pit_choice + 6
        # If current turn is none. The game has just began, set turn to player 1 as default
        # DO NOT ENFORCE PLAYER TURN RULE FOR EASIER TESTING. UN-HASH THIS IN REAL GAME
        # if self._current_turn is None:
        # self._current_turn = 1
        # if player turn out of sequence, return and wait until the right player turn play
        # DO NOT ENFORCE PLAYER TURN RULE FOR EASIER TESTING. UN-HASH THIS IN REAL GAME
        # if player_turn != self._current_turn:
        # return
        # Validate if pit is empty or not. If empty cannot choose this pit
        if self.check_end_game():
            # Check the current state of the game. If Game is ended and do not make any move
            return "Game is ended"
        self._player_list[player_turn].get_player_board()[str(pit_choice)] == 0
        # Going to the player move function
        self.player_move(player_turn, pit_choice)
        # Checking for game condition after making the move. If the game is end, return Game is end.
        self.check_end_game()
        result = list()
        # Looping through player 1 board pit
        for value in self._player_list[1].get_player_board().values():
            # Appending value to result
            result.append(value)
        # Looping through player 1 board pit
        for value in self._player_list[2].get_player_board().values():
            # Appending value to result
            result.append(value)
        return result

    def print_board(self):
        """Print out current board game"""
        # Clear out last game score
        self._game_board_score.clear()
        # Iterate through the dict of player board to get back just the values of each pit
        for value in self._player_list[1].get_player_board().values():
            # Adding value to the game board score
            self._game_board_score.append(value)
        for value in self._player_list[2].get_player_board().values():
            self._game_board_score.append(value)
        print(f"player1:\nstore: {self._player_list[1].get_player_board()['store_1']}")
        print(self._game_board_score[0:6])
        print(f"player2:\nstore: {self._player_list[2].get_player_board()['store_2']}")
        print(self._game_board_score[7:13])

    def return_winner(self):
        """Return winner or tie or game not end yet"""
        player_1_score = int()
        player_2_score = int()
        # Looping through player 1 score
        for num in range(1, 7):
            player_1_score += self._player_list[1].get_player_board()[str(num)]
        # Looping through player 2 score
        for num in range(7, 13):
            player_2_score += self._player_list[2].get_player_board()[str(num)]
        # If one of the player pit has emptied out all pit. Game end.
        if player_1_score == 0 or player_2_score == 0:
            # Adding score to player 1 score as going
            player_1_score += self._player_list[1].get_player_board()['store_1']
            # Adding score to player 2 score as going
            player_2_score += self._player_list[2].get_player_board()['store_2']
            if player_1_score == player_2_score:
                return "It's a tie"
            elif player_1_score > player_2_score:
                return f"Winner is player 1: {self._player_list[1].get_player_name()}"
            elif player_2_score > player_1_score:
                return f"Winner is player 2: {self._player_list[2].get_player_name()}"
        else:
            return "Game has not ended"
