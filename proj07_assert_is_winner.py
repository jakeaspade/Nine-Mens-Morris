import NMM
from proj07 import is_winner

instructor_board_1 = """
    Instructor's Board Not-Win
    7 [ ]------[ ]------[X]
    6  | [X]---[O]---[O] |
    5  |  | [ ][ ][ ] |  |
    4 [O][O][O]   [ ][O][X]
    3  |  | [ ][X][ ] |  |
    2  | [X]---[X]---[ ] |
    1 [X]------[X]------[X]
       a  b  c  d  e  f  g
   """
board_1 = NMM.Board()
board_1.assign_piece("X","b6")
board_1.assign_piece("X","b2")
board_1.assign_piece("X","a1")
board_1.assign_piece("X","d1")
board_1.assign_piece("X","g1")
board_1.assign_piece("X","g4")
board_1.assign_piece("X","g7")
board_1.assign_piece("X","d2")
board_1.assign_piece("X","d3")
board_1.assign_piece("O","d6")
board_1.assign_piece("O","f6")
board_1.assign_piece("O","f4")
board_1.assign_piece("O","a4")
board_1.assign_piece("O","b4")
board_1.assign_piece("O","c4")
instructor_board_2 = """
    Instructor's Board Win
    7 [ ]------[ ]------[X]
    6  | [X]---[O]---[ ] |
    5  |  | [ ][ ][ ] |  |
    4 [ ][ ][ ]   [ ][O][X]
    3  |  | [ ][X][ ] |  |
    2  | [X]---[X]---[ ] |
    1 [X]------[X]------[X]
       a  b  c  d  e  f  g
    """
board_2 = NMM.Board()
board_2.assign_piece("X","b6")
board_2.assign_piece("X","b2")
board_2.assign_piece("X","a1")
board_2.assign_piece("X","d1")
board_2.assign_piece("X","g1")
board_2.assign_piece("X","g4")
board_2.assign_piece("X","g7")
board_2.assign_piece("X","d2")
board_2.assign_piece("X","d3")
board_2.assign_piece("O","d6")
board_2.assign_piece("O","f4")
instructor_not_win = False
instructor_win = True
student_not_win = is_winner(board_1,"X")
student_win = is_winner(board_2,"X")
print(instructor_board_1)
print(instructor_board_2)
print("Instructor's 'X' 'not_win':", instructor_not_win) 
print("Student's 'X' 'not_win':   ", student_not_win)
print("Instructor's 'X' 'win':", instructor_win)
print("Student's 'X' 'win':   ", student_win)
assert instructor_not_win == student_not_win and instructor_win == student_win
