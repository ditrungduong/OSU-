class Player:
    """Represent player"""

    def __init__(self, name, player_num, player_board, opposite_board):
        self._player_name = name
        self._player_num = player_num
        self._player_board = player_board
        self._player_game_board_seq = {'1': '2', '2': '3', '3': '4', '4': '5', '5': '6',
                                       '6': 'store_1', 'store_1': '7', '7': '8', '8': '9',
                                       '9': '10', '10': '11', '11': '12', '12': 'store_2',
                                       'store_2': '1'}
        self._player_opposite_pit = {'1': '7', '2': '8', '3': '9', '5': '11', '6': '12',
                                     '7': '1', '8': '2', '9': '3', '11': '5', '12': '6'}
        self._opposite_board = opposite_board

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
        self._opposite_board = {'1': '7', '2': '8', '3': '9', '5': '11', '6': '12',
                                '7': '1', '8': '2', '9': '3', '11': '5', '12': '6'}
        self._game_board_sequence = {'1': '2', '2': '3', '3': '4', '4': '5', '5': '6',
                                     '6': '7', '7': 'store_1', 'store_1': '8', '8': '9',
                                     '9': '10', '10': '11', '11': '12', '12': 'store_2',
                                     'store_2': '1'}

        self._player_1_board = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, 'store_1': 0}
        self._player_2_board = {'7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, 'store_2': 25}
        self._player_2_oppo_board = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, 'store_1': 0}
        self._player_1_oppo_board = {'7': 4, '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, 'store_2': 0}

    def get_board_map(self, player_num):
        """Return player board base on player number input"""
        if player_num == 1:
            return self._player_1_board
        return self._player_2_board

    def get_player_oppo_board(self, player_num):
        """Return opponent board """
        if player_num == 1:
            return self._player_1_oppo_board
        return self._player_2_oppo_board


class Mancala:
    """Represent Mancala game class"""

    def __init__(self):
        self._player_list = {}
        self._current_turn = None
        self._game_board = Board()
        self._game_board_score = []
        self._current_game_board = []

    # def update_current_board(self):
    # """Set a new board game"""
    # self._current_game_board.append(self._player_list[1].get_player_board())
    # self._current_game_board.append(self._player_list[2].get_player_board())

    def create_player(self, new_player_name):
        """Creating new player and add to the player list"""
        # if player list already has value - player 1 already exist - player 2 will be created
        if self._player_list:
            # Assigning player 2 : Player 2 attribute with name, player number, player board, and opponent board)
            self._player_list[2] = Player(new_player_name, 2, self._game_board.get_board_map(2),
                                          self._game_board.get_player_oppo_board(2))
        else:
            self._player_list[1] = Player(new_player_name, 1, self._game_board.get_board_map(1),
                                          self._game_board.get_player_oppo_board(1))

    def print_board(self):
        """Print out current board game"""
        self._game_board_score.clear()
        for value in self._player_list[1].get_player_board().values():
            self._game_board_score.append(value)
        for value in self._player_list[2].get_player_board().values():
            self._game_board_score.append(value)
        print(f"player1:\nstore: {self._player_list[1].get_player_board()['store_1']}")
        print(self._game_board_score[0:6])
        print(f"player2:\nstore: {self._player_list[2].get_player_board()['store_2']}")
        print(self._game_board_score[7:13])

    def pit_validation(self, player_turn, pit_num):
        """Validate if the pit is available to select"""
        if (player_turn == 1 and str(pit_num) not in self._player_list[1].get_player_board()) or (
                player_turn == 2 and str(pit_num) not in self._player_list[2].get_player_board()):
            return False
        if 1 <= pit_num <= 6:
            if self._player_list[1].get_player_board()[str(pit_num)] == 0:
                print("This pit is empty. Please pick a different pit")
                return False
        else:
            if self._player_list[2].get_player_board()[str(pit_num)] == 0:
                print("This pit is empty. Please pick a different pit")
                return False

    def player_move(self, player_turn, pit_number):
        """Making move"""
        # Get seed amount from the using pit number
        seed_to_go = self._player_list[player_turn].get_player_board()[str(pit_number)]
        self._player_list[player_turn].get_player_board()[str(pit_number)] = 0  # Set seed amount to 0 after take out
        while seed_to_go > 0:  # Continue placing seed until empty
            pit_number = self._player_list[player_turn].get_game_board_seq()[str(pit_number)]  # Move to next pit
            if (player_turn == 1 and pit_number == 'store_2') or (
                    player_turn == 2 and pit_number == 'store_1'):
                continue  # Skip opponent store
            if player_turn == 1 and pit_number == '7':  # adding seed to store 1
                self._player_list[player_turn].get_player_board()['store_1'] += 1
            elif player_turn == 2 and pit_number == '13':  # adding seed to store 2
                self._player_list[player_turn].get_player_board()['store_2'] += 1
            else:
                # Adding seed to each pit
                if pit_number == 'store_1' or pit_number == 'store_2':
                    self._player_list[player_turn].get_player_board()[str(pit_number)] += 1

                elif 1 <= int(pit_number) <= 6 or pit_number == 'store_1':
                    player_turn = 1
                    self._player_list[player_turn].get_player_board()[str(pit_number)] += 1
                else:
                    player_turn = 2
                    self._player_list[player_turn].get_player_board()[str(pit_number)] += 1
            seed_to_go -= 1  # Removing seed after placing

        # Check if last placing seed was in an empty pit, gain opposite pit's seeds.
        if pit_number == 'store_1' or pit_number == 'store_2':
            None

        elif player_turn == 1 and str(pit_number) in self._player_list[player_turn].get_player_board() and \
                self._player_list[player_turn].get_player_board()[str(pit_number)] == 1:
            opposite_pit = self._player_list[player_turn].get_opposite_pit()[str(pit_number)]
            opposite_pit_value = self._player_list[2].get_player_board()[opposite_pit]
            self._player_list[player_turn].get_player_board()['store_1'] = opposite_pit_value
            self._player_list[2].get_player_board()[str(opposite_pit)] = 0

        elif player_turn == 2 and str(pit_number) in self._player_list[player_turn].get_player_board() and \
                self._player_list[player_turn].get_player_board()[str(pit_number)] == 1:
            opposite_pit = self._player_list[player_turn].get_opposite_pit()[str(pit_number)]
            opposite_pit_value = self._player_list[1].get_player_board()[opposite_pit]
            self._player_list[player_turn].get_player_board()['store_2'] = opposite_pit_value
            self._player_list[1].get_player_board()[str(opposite_pit)] = 0

        if (pit_number == 'store_1' and player_turn == 1) or (pit_number == 'store_2' and player_turn == 2):
            # If the last seed landed in the player's store, take another turn.
            print(f"Player {player_turn} take another turn")
            self._current_turn = player_turn
        else:
            # Rotating player turn
            if player_turn == 1:
                self._current_turn = 2
                return
            elif player_turn == 2:
                self._current_turn = 1
                return

    def play_game(self, player_turn, pit_choice):
        """Start game, passing players number and turns pit choice, add participating player to player_list dictionary,
        iterate through turns list to move tokens, return a list of seed amount for each of the pit.
        """
        result = []

        if self._current_turn is None:
            self._current_turn = 1
            # if player turn out of sequence, return and wait until the right player turn play
        if player_turn != self._current_turn:
            return
        elif self.pit_validation(player_turn, pit_choice) is False:
            return
        elif self.return_winner() != 'Game has not ended':
            return
        else:
            self.player_move(player_turn, pit_choice)

        for value in self._player_list[1].get_player_board().values():
            result.append(value)
        for value in self._player_list[2].get_player_board().values():
            result.append(value)
        return result

    def return_winner(self):
        """Return winner or tie or game not end yet"""
        player_1_score = int()
        player_2_score = int()
        # looping through player pit
        for num in range(1, 7):
            # adding player score after each iteration
            player_1_score += self._player_list[1].get_player_board()[str(num)]
        for num in range(7, 13):
            player_2_score += self._player_list[2].get_player_board()[str(num)]
        if player_1_score == 0 or player_2_score == 0:
            player_1_score += self._player_list[1].get_player_board()['store_1']
            player_2_score += self._player_list[2].get_player_board()['store_2']
            if player_1_score == player_2_score:
                return "It's a tie"
            elif player_1_score > player_2_score:
                return f"Winner is player 1 {self._player_list[1].get_player_name()}"
            elif player_2_score > player_1_score:
                return f"Winner is player 2: {self._player_list[2].get_player_name()}"
        else:
            return "Game has not ended"


game = Mancala()
player1 = game.create_player("Lily")
player2 = game.create_player("Lucy")
game.play_game(1, 1)
game.play_game(1, 2)
game.play_game(1, 3)
game.play_game(1, 4)
game.play_game(1, 5)
game.play_game(1, 6)
game.print_board()
print(game.return_winner())
