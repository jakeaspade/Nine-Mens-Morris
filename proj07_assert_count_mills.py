import NMM
from proj07 import count_mills

instructor_board = """
    Instructor's Board
    7 [ ]------[ ]------[X]
    6  | [ ]---[O]---[O] |
    5  |  | [ ][ ][ ] |  |
    4 [O][O][O]   [ ][O][X]
    3  |  | [ ][X][ ] |  |
    2  | [X]---[X]---[ ] |
    1 [X]------[X]------[X]
       a  b  c  d  e  f  g
   """
board = NMM.Board()
board.assign_piece("X","b2")
board.assign_piece("X","a1")
board.assign_piece("X","d1")
board.assign_piece("X","g1")
board.assign_piece("X","g4")
board.assign_piece("X","g7")
board.assign_piece("X","d2")
board.assign_piece("X","d3")
board.assign_piece("O","d6")
board.assign_piece("O","f6")
board.assign_piece("O","f4")
board.assign_piece("O","a4")
board.assign_piece("O","b4")
board.assign_piece("O","c4")
X_mill_count = count_mills(board,'X')
O_mill_count = count_mills(board,'O')
print(instructor_board)
print("Instructor's 'X' mill count: 3")
print("Instructor's 'O' mill count: 1")
print("Student's 'X' mill count:", X_mill_count)
print("Student's 'O' mill count:", O_mill_count)
assert X_mill_count == 3 and O_mill_count == 1
