# -*- coding: utf-8 -*-
'''
You've mastered the Rubik's Cube and got bored solving it, 
so now you are looking for a new challenge. 
One puzzle similar to the Rubik's Cube caught your attention. 
It's called a Pyraminx puzzle, 
and is a triangular pyramid-shaped puzzle. 
The parts are arranged in a pyramidal pattern on each side, 
while the layers can be rotated with respect to each vertex, 
and the individual tips can be rotated as well. 
There are 4 faces on the Pyraminx. 
The puzzle should be held so that one face faces you and one face faces down, 
as in the image below. 
The four corners are then labeled U (for up), 
R (for right), L (for left), and B (for back). 
The front face thus contains the U, R, and L corners.
'''
import unittest

def pyraminxPuzzle(face_colours, moves):
    move_position = {"U": [[0, 0], [3, 8], [2, 4]],
                     "u": [[0, 0], [0, 1], [0, 2], [0, 3], [3, 8], [3, 3], [3, 7], [3, 6], [2, 4], [2, 6], [2, 5], [2, 1]],
                     "L": [[2, 0], [1, 8], [0, 4]],
                     "l": [[2, 0], [2, 1], [2, 2], [2, 3], [1, 8], [1, 3], [1, 7], [1, 6], [0, 4], [0, 6], [0, 5], [0, 1]],
                     "R": [[3, 0], [0, 8], [1, 4]],
                     "r": [[3, 0], [3, 1], [3, 2], [3, 3], [0, 3], [0, 8], [0, 7], [0, 6], [1, 4], [1, 6], [1, 5], [1, 1]],
                     "B": [[1, 0], [2, 8], [3, 4]],
                     "b": [[1, 0], [1, 1], [1, 2], [1, 3], [2, 8], [2, 3], [2, 7], [2, 6], [3, 4], [3, 6], [3, 5], [3, 1]]
                     }
    puzzle = [[c for _ in range(9)] for c in face_colours]
    move_colors = update_move_colors(puzzle, move_position)
    reverse_move = [move + "'" if "'" not in move else move[0] for move in moves[::-1]]

    for move in reverse_move:
        left = "'" in move
        current_color = shift_color(move_colors[move[0]], left)
        update_cube(puzzle, move_position[move[0]], current_color)
        move_colors = update_move_colors(puzzle, move_position)

    #print_cube(puzzle)
    return puzzle

def update_move_colors(puzzle, move_position):
  move_colors = {}
  for move in move_position:
      move_colors[move] = [puzzle[r][c] for r,c in move_position[move]]
  return move_colors

def shift_color(current_color, left):
  for _ in range(len(current_color) // 3):
    if left:
        current_color = current_color[1:] + [current_color[0]]
    else:
        current_color =  [current_color[-1]] + current_color[:-1]
  return current_color


def update_cube(cube, current_positions, current_colors):
  for i in range(len(current_positions)):
      r, c = current_positions[i]
      cube[r][c] = current_colors[i]

def print_cube(cube):
    print("\n".join(",".join(c) for c in cube))

class TestPyraminx(unittest.TestCase):
    def test1(self):
        exp_1 = [["Y","Y","Y","Y","R","R","R","R","G"],
                 ["G","R","O","O","O","G","G","G","G"],
                 ["Y","O","Y","G","O","O","G","G","Y"],
                 ["R","O","O","R","O","Y","Y","R","R"]]
        colours = ["R",  "G",  "Y",  "O"]
        moves = ["B",  "b'",  "u'",  "R"]
        self.assertEqual(pyraminxPuzzle(colours, moves), exp_1)

    def test2(self):
        exp_2 = [["R","R","R","R","R","R","R","R","R"],
                 ["G","G","G","G","G","G","G","G","G"],
                 ["Y","Y","Y","Y","Y","Y","Y","Y","Y"],
                 ["O","O","O","O","O","O","O","O","O"]]
        colours = ["R",  "G",  "Y",  "O"]
        moves = ["l",  "l'"]
        self.assertEqual(pyraminxPuzzle(colours, moves), exp_2)

    def test3(self):
        exp_3 = [["Y","O","R","G","G","G","G","G","G"],
                 ["G","O","G","Y","O","O","Y","Y","Y"],
                 ["R","G","R","R","O","Y","Y","Y","Y"],
                 ["R","R","R","R","O","O","O","O","R"]]
        colours = ["R",  "G",  "Y",  "O"]
        moves = ["l",  "l'",  "u",  "R",  "U'",  "L",  "R'",  "u'",  "l'",  "L'",  "r"]
        self.assertEqual(pyraminxPuzzle(colours, moves), exp_3)

    def test4(self):
        exp_4 = [["R","R","R","G","R","R","G","G","G"],
                 ["G","O","G","G","O","O","O","G","G"],
                 ["Y","Y","Y","Y","Y","Y","Y","Y","Y"],
                 ["R","R","R","R","O","O","O","O","O"]]
        colours = ["R",  "G",  "Y",  "O"]
        moves = ["r"]
        self.assertEqual(pyraminxPuzzle(colours, moves), exp_4)

    def test5(self):
        exp_5 = [["A","A","A","A","A","A","A","A","A"],
                 ["B","B","B","B","B","B","B","B","B"],
                 ["C","C","C","C","C","C","C","C","C"],
                 ["D","D","D","D","D","D","D","D","D"]]
        colours = ["A",  "B",  "C",  "D"]
        moves = ["l",  "l'",  "r'",  "r",  "u",  "U",  "u'",  "R'",  "L",  "R",  "L'",  "B'",  "U'",  "b",  "B",  "b'"]
        self.assertEqual(pyraminxPuzzle(colours, moves), exp_5)

if __name__ == '__main__':
    unittest.main()
