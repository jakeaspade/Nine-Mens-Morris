import NMM
from proj07 import points_not_in_mills

instructor_board = """
    Instructor's Board
    7 [ ]------[ ]------[X]
    6  | [X]---[O]---[O] |
    5  |  | [ ][ ][ ] |  |
    4 [O][O][O]   [ ][O][X]
    3  |  | [ ][X][ ] |  |
    2  | [X]---[X]---[ ] |
    1 [X]------[X]------[X]
       a  b  c  d  e  f  g
   """
instructor_X = ['b2', 'b6']
instructor_O = ['d6', 'f4', 'f6']
board = NMM.Board()
board.assign_piece("X","b6")
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
student_X = sorted(list(points_not_in_mills(board,"X")))
student_O = sorted(list(points_not_in_mills(board,"O")))
print(instructor_board)
print("Instructor's 'X' placed:", instructor_X) 
print("Student's 'X' placed:   ", student_X)
print("Instructor's 'O' placed:", instructor_O)
print("Student's 'O' placed:   ", student_O)
assert instructor_X == student_X and instructor_O == student_O
