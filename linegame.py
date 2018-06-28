# -*- coding: utf-8 -*-
'''
Let's remember the '90s and play an old-school Lines (wikipedia reference) game 
with the following rules.

The game starts with a 9 × 9 field with several colored balls placed on its cells 
(there are 7 possible colors but not all colors have to be present initially). 
The player can move one ball per turn, and they may only move a ball if there is 
a clear path between the current position of the chosen ball and the desired 
destination. Clear paths are formed by neighboring empty cells. 
Two cells are neighboring if they have a common side. 
The goal is to remove balls by forming lines (horizontal, vertical or diagonal) 
of at least five balls of the same color. 
If the player manages to form one or more such lines, 
the move is called successful, and the balls in those lines disappear. 
Otherwise, the move is called unsuccessful, and three more balls appear 
on the field.

You are given the game logs, and your task is to calculate the player's 
final score. Here's the information you have:

The field state at the initial moment;
The clicks the user has made. Note that a click does not necessarily result 
in a move:
If the user clicks a ball and then another, the first click is ignored;
If two consecutive clicks result in an incorrect move, they are ignored;
After each unsuccessful move three more balls appear:
newBalls contains the balls' colors;
newBallsCoordinates contains their coordinates;
Note that after the balls appear, new lines may form;
Whenever new lines appear, they are removed and the player 
receives A + B - 1 points, where:
A is the number of lines of at least five balls;
B is the total number of balls in those lines;
Possible ball colors are red, blue, orange, violet, green, yellow and cyan, 
which are represented in logs by
"R", "B", "O", "V", "G", "Y" and "C" respectively.
'''
import unittest

def linesGame(field, clicks, newBalls, newBallsCoordinates):
    chosen_ball = None
    newball_idx = 0
    score = 0
    for click in clicks:
        r, c = click
        if field[r][c] != ".":
            chosen_ball = click
            continue          
        if chosen_ball is not None and field[r][c] == ".":
            if not move_available(field, chosen_ball, click):
                continue
            move_ball(field, chosen_ball, click)
            chosen_ball = None

            s = check_lines(field, click)
            if s == 0:
                insert_newballs(field, 
                                newBalls[newball_idx:newball_idx+3], 
                                newBallsCoordinates[newball_idx:newball_idx+3])
                for coordinate in newBallsCoordinates[newball_idx:newball_idx+3]:
                    s += check_lines(field, coordinate)
                newball_idx += 3
                
            score += s
    return score

def insert_newballs(field, balls, coordinates):
    for i in range(len(coordinates)):
        r, c = coordinates[i]
        ball = balls[i]
        field[r][c] = ball

def move_available(field, placeA, placeB):
    moved = set()
    next_moves = set()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    next_start = placeA
    while True:
        if next_start == placeB:
            return True
        moved.add(trans_coordinate_2_string(next_start))
        moves = []
        for direction in directions:
            r, c = next_start[0]+direction[0], next_start[1]+direction[1]
            if moveable_point(field, r, c):
                if trans_coordinate_2_string([r,c]) in moved:
                    continue
                next_moves.add(trans_coordinate_2_string([r,c]))
                moves += [[r,c]]
        if len(moves) > 0:
            next_start = moves[0]
            next_moves.remove(trans_coordinate_2_string(next_start))
        else:
            if len(next_moves) == 0:
                return False
            next_start = trans_string_2_coordinate(next_moves.pop())

def moveable_point(field, r, c):
    return 0 <= r < 9 and 0 <= c < 9 and field[r][c] == "."

def trans_coordinate_2_string(coordinate):
    return f"{coordinate[0]},{coordinate[1]}"

def trans_string_2_coordinate(coordinate_string):
    return list(map(int, coordinate_string.split(",")))

def move_ball(field, placeA, placeB):
    ra, ca = placeA
    rb, cb = placeB
    field[rb][cb] = field[ra][ca]
    field[ra][ca] = "."


def check_lines(field, position):
    target_color = field[position[0]][position[1]]
    directions = [([0, 1], [0, -1]), ([1, 0], [-1, 0]), ([-1, 1], [1, -1]), ([1, 1], [-1, -1])]
    lines = []
    for direction in directions:
        continue_piece = set()
        for i in range(2):
            p = position[:]
            while 0 <= p[0] < 9 and 0 <= p[1] < 9:
                if field[p[0]][p[1]] == target_color:
                    continue_piece.add(trans_coordinate_2_string(p))
                else:
                    break
                p[0] += direction[i][0]
                p[1] += direction[i][1]
        if len(continue_piece) >= 5:
            lines.append(list(continue_piece))
    
    remove_pieces(field, lines)
    return len(lines) + sum(len(ball) for ball in lines) - 1 if len(lines) > 0 else 0
    
def remove_pieces(field, positions):
    for position in positions:
        for p in position:
            r,c = trans_string_2_coordinate(p)
            field[r][c] = "."


class TestPyraminx(unittest.TestCase): 
    def test1(self):
        field = [['.', 'G', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', 'V', '.'],
                 ['.', 'O', '.', '.', 'O', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', 'O'],
                 ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['R', '.', '.', '.', '.', '.', '.', 'B', 'R'],
                 ['.', '.', 'C', '.', '.', '.', '.', 'Y', 'O']]
        clicks = [[4, 8], [2, 1], [4, 4], [6, 4], [4, 8], [1, 2], [1, 4], [4, 8], [6, 4]]
        newBalls = ['R', 'V', 'C', 'G', 'Y', 'O']
        newBallsCoordinates = [[1, 2], [8, 5], [8, 6], [1, 1], [1, 8], [7, 4]]
        self.assertEqual(linesGame(field, clicks, newBalls, newBallsCoordinates), 6)

    def test2(self):
        field = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'],
                 ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', 'O'],
                 ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
                 ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
        clicks = [[4, 8], [4, 4]]
        newBalls = []
        newBallsCoordinates = []
        self.assertEqual(linesGame(field, clicks, newBalls, newBallsCoordinates), 17)

    def test3(self):
        field = [["V",".",".",".",".",".",".",".","."], 
                 ["V",".",".",".",".",".",".",".","V"], 
                 ["V",".","O",".","O",".","O",".","."], 
                 ["V",".",".","O","O","O",".",".","."], 
                 [".","V","V","V",".",".",".",".","O"], 
                 ["V",".",".","O","O","O",".",".","."], 
                 ["V",".","O",".","O",".","O",".","."], 
                 ["V",".",".",".",".",".",".",".","."], 
                 ["V",".",".",".",".",".",".",".","."]]
        clicks = [[4,8], [4,4], [1,8], [4,0]] 
        newBalls = []
        newBallsCoordinates = []
        self.assertEqual(linesGame(field, clicks, newBalls, newBallsCoordinates), 17)

    def test4(self):
        field = [[".",".",".","G","G",".",".","G","."], 
                 ["G",".",".",".",".",".",".","G","."], 
                 [".","G",".",".",".",".",".","G","."], 
                 [".",".","G",".",".",".",".","G","G"], 
                 ["G","G","G",".","G","G",".",".","."], 
                 [".",".",".",".","G",".","G","G","."], 
                 [".",".",".",".",".","G",".",".","."], 
                 [".",".",".",".","G",".",".",".","."], 
                 [".",".",".","G",".",".",".",".","."]]
        clicks = [[0,3], [4,7], [0,4], [4,3]]
        newBalls = []
        newBallsCoordinates = []
        self.assertEqual(linesGame(field, clicks, newBalls, newBallsCoordinates), 25)

if __name__ == "__main__":
    unittest.main()

