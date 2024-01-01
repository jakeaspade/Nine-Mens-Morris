import NMM
from proj07 import placed

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
instructor_X = ['a1', 'b2', 'd1', 'd2', 'd3', 'g1', 'g4', 'g7']
instructor_O = ['a4', 'b4', 'c4', 'd6', 'f4', 'f6']
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
student_X = sorted(list(placed(board,"X")))
student_O = sorted(list(placed(board,"O")))
print(instructor_board)
print("Instructor's 'X' placed:", instructor_X) 
print("Student's 'X' placed:   ", student_X)
print("Instructor's 'O' placed:", instructor_O)
print("Student's 'O' placed:   ", student_O)
assert instructor_X == student_X and instructor_O == student_O
