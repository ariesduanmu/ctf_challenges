# -*- coding: utf-8 -*-
'''
John has always liked analog clocks more than digital ones.
He's been dreaming about turning his digital clock into an analog one for as
long as he can remember, 
and now he met you, a great programmer, so his dream is about to come true.

The screen of his digital clock is a simple 17 × 17 rectangle of pixels.
It always shows four digits: the first two stand for hours and second two
for minutes (John's clock uses the 24-hour format). Each digit is located
in a 17 × 4 rectangle, with the leftmost column always empty, and the other
 three columns filled according to this pattern with the proper scaling:

After the first two digits there is a separating column containing one symbol
':' at its center.

Now John asks you to make his clock show time in the format similar to
analog clocks. Here's how: an analog clock can be represented as a
circle (the clock's borders) and two segments (the clock's hands).
To show it on the 17 × 17 screen, you should light the pixels on it so
that the pixel with coordinates (x, y) is enabled if and only if the minimal
distance to the circle or one of the segments is less than sqrt(0.5).

John wants you to implement the function that changes the digital representation
to the analog one as described above. Given a 17 × 17 rectangle dtime
representing digital time representation, return the analog representation
of the same time.

Please note that for the early prototype you have to develop,
both of the clock's hands should have the same length.
'''

import math
import unittest

def read_numbers(dtime):
    num = {
        "******." : "0",
        "*..*..*" : "1",
        "**.**.*" : "2",
        "****..*" : "3",
        ".**..**" : "4",
        "*.**.**" : "5",
        "*.*****" : "6",
        "***...." : "7",
        "*******" : "8",
        "****.**" : "9"
    }
    time = ""
    positions=((0,1),(4,2),(12,2),(16,1),(12,0),(4,0),(8,1))
    for i in [1, 5, 10, 14]:
        n = "".join(dtime[p[0]][p[1] + i] for p in positions)
        if n in num:
            time += num[n]
    return time
    

def get_pos(i, r=9):
    a, b = math.sin(2 * math.pi * i / 60) * r, math.cos(2 * math.pi * i / 60) * r
    x, y = int(a), int(b)
    if 0 <= x + 8 < 17 and 0 <= 8 - y < 17:
        return (x + 8, 8 - y)
    return None

def hand_pos(i, r=9):
    a, b = math.sin(2 * math.pi * i / 60) * r, math.cos(2 * math.pi * i / 60) * r
    return (a+8, 8-b)
    
def clock_hand(i, r=8):
    hand = []
    while r > 0:
        hand += [hand_pos(i, r)]
        r -= 0.1
    
    return hand
    
def distance(a, b):
    return (a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2 

def clock(time):
    hours = int(time[0:2]) % 12
    minutes = int(time[2:])
    
    clock = [["." for _ in range(17)] for _ in range(17)]
    
    steps = [x * 0.5 for x in range(0, 120)]
    points = [get_pos(i) for i in steps if get_pos(i) is not None]
    for x, y in points:
        clock[x][y] = "*"    

    hour_hands = clock_hand((hours + minutes / 60) * 5)    
    minute_hands = clock_hand(minutes)
    
    for hand in hour_hands + minute_hands:
        for i in range(17):
            for j in range(17):                
                d = distance((i,j), hand)
                if d <= 0.5:
                    clock[j][i] = "*"

    
    return clock
    

def timeASCIIRepresentation(dtime):
    time = read_numbers(dtime)
    return clock(time)