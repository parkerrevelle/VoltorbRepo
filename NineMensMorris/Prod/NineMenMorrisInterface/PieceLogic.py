#todo add moveValidator,




class Locations:
    def __init__(self):
        # 24 positions initialized to 0 (empty)
        self.board = [0] * 24
        self.current_player = 1  # Start with player 1
        # Define valid positions on the board
        self.valid_positions = set(range(24))
        # Track total number of pieces for each player
        self.piece_count = {1: 9, 2: 9}
        # Track how many pieces have been placed on the board
        self.pieces_placed = {1: 0, 2: 0}
        #active turn count
        self.turn_count = 0
        #bool for if player can fly
        self.can_fly = {1: False, 2: False}
        #value for player phases: 1 is placing pieces, 2 is moving pieces, 3 is flying pieces
        self.player_phases = {1: 1, 2: 1}
        

    def place_piece(self, position):
        """
        Place a piece on the board.
        :param position: int, position on the board (0-23)
        :return: bool, True if the piece was placed successfully, False otherwise
        """
        
        if position in self.valid_positions and self.board[position] == 0:
            self.board[position] = self.current_player
            return True
        else:
            print("Invalid move. Try again.")
            return False

    def fly_piece(self, from_position, to_position):
        """
        Fly a piece from one position to another.
        :param from_position: int, starting position (0-23)
        :param to_position: int, ending position (0-23)
        :return: bool, True if the piece was flown successfully, False otherwise
        """
        # Check if the player is allowed to fly a piece
        if self.piece_count[self.current_player] > 3:
            print("Cannot fly pieces unless you have only 3 pieces left.")
            return False
        # Check if the starting position contains the player's piece
        if self.board[from_position] != self.current_player:
            print("Invalid starting position.")
            return False
        # Check if the ending position is valid and empty
        if to_position not in self.valid_positions or self.board[to_position] != 0:
            print("Invalid ending position.")
            return False
        # Move the piece
        self.board[from_position] = 0
        self.board[to_position] = self.current_player
        return True

    def switch_player(self):
        """
        Switch the current player.
        """
        self.current_player = 3 - self.current_player  # Switches between 1 and 2


    def is_mill(self, position):
        """
        Check if placing a piece in the given position forms a mill.
        :param position: int, position on the board (0-23)
        :return: bool, True if a mill is formed, False otherwise
        """
        # Define all possible mills
        mills = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal mills in the outer square
            [9, 10, 11], [12, 13, 14], [15, 16, 17],  # Horizontal mills in the middle square
            [18, 19, 20], [21, 22, 23],  # Horizontal mills in the inner square
            [0, 9, 21], [3, 10, 18], [6, 11, 15],  # Vertical mills in the left side
            [1, 4, 7], [16, 19, 22],  # Vertical mills in the middle
            [8, 12, 17], [5, 13, 20], [2, 14, 23]  # Vertical mills in the right side
        ]
        for mill in mills:
            if position in mill:
                if all(self.board[pos] == self.current_player for pos in mill):
                    return True
        return False

    def remove_opponent_piece(self, position):
        """
        Remove an opponent's piece from the board.
        :param position: int, position on the board (0-23)
        :return: bool, True if the piece was removed successfully, False otherwise
        """
        opponent = 3 - self.current_player
        if self.board[position] == opponent:
            self.board[position] = 0
            self.piece_count[3 - self.current_player] =- 1
            return True
        else:
            print("Invalid removal. Try again.")
            return False
    
    def move_piece(self, moveFrom, moveTo):
        neighbors = {
        0: [1, 3, 8],
        1: [0, 2, 4],
        2: [1, 5, 13],
        3: [0, 4, 6, 9],
        4: [1, 3, 5],
        5: [2, 4, 7, 12],
        6: [3, 7, 10],
        7: [5, 6, 11],
        8: [0, 9, 20],
        9: [3, 8, 10, 17],
        10: [6, 9, 14],
        11: [7, 12, 16],
        12: [5, 11, 13, 19],
        13: [2, 12, 22],
        14: [10, 15, 17],
        15: [14, 16, 18],
        16: [11, 15, 19],
        17: [9, 14, 18, 20],
        18: [15, 17, 19, 21],
        19: [12, 16, 18, 22],
        20: [8, 17, 21],
        21: [18, 20, 22],
        22: [13, 19, 21],
        }
        
        if moveTo in neighbors.get(moveFrom, []) and self.board[moveTo] == 0 and self.current_player == self.board[moveFrom]:
          self.board[moveTo] = self.board[moveFrom]
          self.board[moveFrom] = 0
          return True
        else: 
          print("Invalid Location.")
          return False

    def is_game_over(self):
        """
        Check game state to see if game over has been accomplished
        """
        if self.piece_count.get(1) <= 2:
            return True
        if self.piece_count.get(2) <= 2:
            return True
        else:
            return False

    def increment_turn(self):
        self.turn_count += 1

    
            
        




