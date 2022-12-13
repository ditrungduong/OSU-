class Board:
    def __init__(self):
        self._opposite_board = {'1': '7', '2': '8', '3': '9', '5': '11', '6': '12',
                                '7': '1', '8': '2', '9': '3', '11': '5', '12': '6'}
        self._game_board_sequence = {'1': '2', '2': '3', '3': '4', '4': '5', '5': '6',
                                     '6': '7', '7': 'store_1', 'store_1': '8', '8': '9',
                                     '9': '10', '10': '11', '11': '12', '12': 'store_2',
                                     'store_2': '1'}

        self._player_1_board = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, 'store_1': 0}
        self._player_2_board = {'7': 4, '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, 'store_2': 0}
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
