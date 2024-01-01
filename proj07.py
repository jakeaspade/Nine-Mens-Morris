###############################################################################
#   Computer Project #7
#
#   While loop to play the game:
#       Phase 1:
#           Prompt for a point to place a piece
#           If point is valid:
#               Place piece
#               If a mill is formed:
#                   Prompt for a piece to remove
#                   Remove piece
#            Switch players
#           Repeat until all pieces are placed
#       Phase 2:
#           Prompt for a move
#           If move is valid:
#               Move piece
#               If a mill is formed:
#                   Prompt for a piece to remove
#                   Remove piece
#           Switch players
#           Repeat until a player has less than 3 pieces
#       If a player has less than 3 pieces:
#           The other player wins
###############################################################################
import sys
import NMM  # This is necessary for the project


BANNER = """
    __      _(_)_ __  _ __   ___ _ __| | |
    \ \ /\ / / | '_ \| '_ \ / _ \ '__| | |
     \ V  V /| | | | | | | |  __/ |  |_|_|
      \_/\_/ |_|_| |_|_| |_|\___|_|  (_|_)
"""

RULES = """                                                                                       
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    The game is ends when a player (the loser) has less than three 
    pieces on the board.
"""

MENU = """
    Game commands (first character is a letter, second is a digit):
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game

"""


## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
def input( prompt=None ):
    if prompt != None:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str


def count_mills(board, player):
    """
    Count the number of mills for a given player
        Args:
            board (NMM.Board): the board to count mills on
            player (str): the player to count mills for
        Returns:
            int: the number of mills for the given player
    """
    mill_count = 0
    for mill in board.MILLS:
        valid_mill = True
        for space in mill:
            if board.points[space] != player:
                # if any space in the mill is not the player's, it is not a mill
                valid_mill = False
                break
        if valid_mill: # if the mill is valid, add one to the mill count
            mill_count += 1
    return mill_count



def place_piece_and_remove_opponents(board, player, destination):
    """
    Takes the given board object and places a piece for the
    given player at the given destination. If the placement forms a mill,
    the player is prompted to remove an opponent's pieces.
        Args:
            board (NMM.Board): the board to place a piece on
            player (str): the player to place a piece for
            destination (str): the point to place a piece at
        Returns:
            None
    """
    try:
        # if the destination is not empty or is the other player's
        if board.points[destination] != " ":
            raise RuntimeError("Invalid command: Not a valid point")
        else:
            previous_mill_count = count_mills(board, player)
            board.assign_piece(player, destination)
            # If a mill was formed, remove a piece
            if previous_mill_count < count_mills(board, player):
                print("A mill was formed!")
                print(board)
                remove_piece(board, get_other_player(player))
    except KeyError:    # if the destination is not a point on the board
        raise RuntimeError("Invalid command: Not a valid point")


def move_piece(board, player, origin, destination):
    """
    Takes the given board object and moves a piece from a starting point to an
    adjacent point. If the move forms a mill, the player is prompted to remove
        Args:
            board (NMM.Board): the board to move a piece on
            player (str): the player to move a piece for
            origin (str): the point to move a piece from
            destination (str): the point to move a piece to
        Returns:
            None
    """
    try:
        # if the destination is not adjacent to the origin
        if not(destination in board.ADJACENCY[origin]):
            raise RuntimeError("Invalid command: Not a valid point")
        # if the origin is not the player's
        elif board.points[origin] != player:
            raise RuntimeError(\
                "Invalid command: Origin point does not belong to player")
        else:
            board.clear_place(origin)
            place_piece_and_remove_opponents(board, player, destination)
    except KeyError:
        raise RuntimeError("Invalid command: Not a valid point")


def points_not_in_mills(board, player):
    """
    Takes the given board object and returns a list of points that are not in
    mills for the given player.
        Args:
            board (NMM.Board): the board to check for mills on
            player (str): the player to check for mills for
        Returns:
            list: a list of points that are not in mills for the given player
    """
    player_spots = placed(board, player)
    collection_of_points = player_spots.copy()
    for mill in board.MILLS:
        if set(mill).issubset(set(player_spots)):
            for point in mill:
                if point in collection_of_points:
                    collection_of_points.remove(point)
    return collection_of_points


def placed(board, player):
    """
    Takes the given board object and returns a list of points that have pieces
    form a given player occupying them.
        Args:
            board (NMM.Board): the board to check for pieces on
            player (str): the player to check for pieces for
        Returns:
            list: a list of points that have pieces from the given player
    """
    player_spots = []
    for point in board.points:
        if board.points[point] == player:
            player_spots.append(point)
    return player_spots


def remove_piece(board, player):
    """
    Takes the given board object and prompts the given player to remove a piece
    from the opponent on the board.  Continues to prompt until a valid piece is
    removed.
        Args:
            board (NMM.Board): the board to remove a piece from
            player (str): the player to remove a piece for
        Returns:
            None
    """
    while True:
        try:
            destination = input("Remove a piece at :> ").strip().lower()
            try:
                # if the destination is not the other player's or is empty
                if destination in placed(board, get_other_player(player)) or \
                        board.points[destination] == ' ':
                    raise RuntimeError(\
                        "Invalid command: Point does not belong to player")
            # if the destination is in a mill unless all points are in mills
                elif not(destination in points_not_in_mills(board, player)) \
                    and points_not_in_mills(board, player) != []:
                    raise RuntimeError('Invalid command: Point is in a mill')
                else:
                    board.clear_place(destination)
                    break
            except KeyError:
                raise RuntimeError("Invalid command: Not a valid point")
        except RuntimeError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))



def is_winner(board, player):
    """
    Takes the given board object and returns True if the given player has won
    the game, False otherwise.
        Args:
            board (NMM.Board): the board to check for a winner on
            player (str): the player to check for a win
        Returns:
            bool: True if the given player has won the game, False otherwise
    """
    if len(placed(board,get_other_player(player))) < 3:
        return True
    else:
        return False
    pass  # stub; delete and replace it with your code


def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"


def main():
    # Loop so that we can start over on reset
    while True:
        # Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0  # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent

        # PHASE 1
        print(player + "'s turn!")
        # placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()
        # Until someone quits or we place all 18 pieces...
        try:
            while command != 'q' and placed_count != 18:
                if command == 'r':  # resets the game
                    raise StopIteration
                try:
                    if command == 'h':  # displays the menu
                        print(MENU)
                        command = input("Place a piece at :> ").strip().lower()
                        continue
                    else:
                        place_piece_and_remove_opponents(\
                            board, player, command)
                        player = get_other_player(player)
                        placed_count += 1

                # Any RuntimeError you raise inside this try lands here
                except RuntimeError as error_message:
                    print("{:s}\nTry again.".format(str(error_message)))
                # Prompt again
                print(board)
                print(player + "'s turn!")
                if placed_count < 18:
                    command = input("Place a piece at :> ").strip().lower()
                else:
                    print("**** Begin Phase 2: \
Move pieces by specifying two points")
                    command = input("Move a piece (source,destination) :> ")\
                        .strip().lower()
                print()
            # PHASE 2 of game
            while command != 'q':
                # commands should have two points
                if command == 'h':  # displays the menu
                    print(MENU)
                    command = input("Move a piece (source,destination) :> ")\
                        .strip().lower()
                    continue
                elif command == 'r':  # resets the game
                    raise StopIteration
                command = command.split()
                try:
                    if len(command) != 2:   # if the command is not two points
                        raise RuntimeError("Invalid number of points")
                    move_piece(board, player, command[0], command[1])
                    player = get_other_player(player)

                # Any RuntimeError you raise inside this try lands here
                except RuntimeError as error_message:
                    print("{:s}\nTry again.".format(str(error_message)))
                    # Display and reprompt
                if is_winner(board,player): # if the player has won
                    print(BANNER)
                    return
                # if the other player has won
                elif is_winner(board, get_other_player(player)):
                    print(BANNER)
                    return
                print(board)
                # display_board(board)
                print(player + "'s turn!")
                command = input("Move a piece (source,destination) :> ")\
                    .strip().lower()
                print()
        except StopIteration:
            continue
        # If we ever quit we need to return
        if command == 'q':
            return


if __name__ == "__main__":
    main()
