from board import Board


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
        self._player_opposite_pit = {'1': '12', '2': '11', '3': '10', '5': '9', '6': '8',
                                     '12': '1', '11': '2', '9': '3', '5': '5', '8': '6'}
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
    def get_oppo_board(self):
        """Return opposite board"""
        return self._opposite_board
    def update_oppo_board(self, new_oppo_board):
        """Update current opposite board"""
        self._opposite_board = new_oppo_board
