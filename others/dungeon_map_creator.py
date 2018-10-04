# -*- coding: utf-8 -*-
from queue import Queue
from random import randint
from collections import namedtuple

Position = namedtuple("Position", ["lx","ly","rx","ry","isplitable"])

def generate_rooms(width, height, min_room_number, min_room_space):
    splitable = Queue()
    splitable.put(Position(0,0,width,height,True))
    unsplitable = Queue()
    while splitable.qsize() + unsplitable.qsize() < min_room_number and splitable.qsize() > 0:
        room = splitable.get()
        room_a, room_b = split_room(room, min_room_space)
        if room_a is not None:
            if room_a.isplitable:
                splitable.put(room_a)
            else:
                unsplitable.put(room_b)

        if room_b is not None:
            if room_b.isplitable:
                splitable.put(room_b)
            else:
                unsplitable.put(room_b)
    return list(splitable.queue) + list(unsplitable.queue)

def split_room(room, min_room_space):
    direction = randint(0, 1)# 0 is horizon 1 is vertical
    if direction == 0:
        return split_room_horizon(room, min_room_space)
    elif direction == 1:
        return split_room_vertical(room, min_room_space)
    return None, None

def split_room_horizon(room, min_room_space):
    padding = (randint(0, (room.ry - room.ly) // 8)) // 2
    split_y = randint(room.ly + (room.ry - room.ly) // 4, room.ry - (room.ry - room.ly) // 4)
    room_a_space = (room.rx - room.lx) * (split_y - padding - room.ly)
    room_a = Position(room.lx, room.ly, room.rx, split_y - padding, room_a_space >= min_room_space)
    room_b_space = (room.rx - room.lx) * (room.ry - split_y - padding)
    room_b = Position(room.lx, split_y + padding, room.rx, room.ry, room_b_space >= min_room_space)
    return room_a, room_b

def split_room_vertical(room, min_room_space):
    padding = (randint(0, (room.rx - room.lx) // 8)) // 2
    split_x = randint(room.lx + (room.rx - room.lx) // 4, room.rx - (room.rx - room.lx) // 4)
    room_a_space = (split_x - padding - room.lx) * (room.ry - room.ly)
    room_a = Position(room.lx, room.ly, split_x - padding, room.ry, room_a_space >= min_room_space)
    room_b_space = (room.rx - split_x - padding) * (room.ry - room.ly)
    room_b = Position(split_x + padding, room.ly, room.rx, room.ry, room_b_space >= min_room_space)
    return room_a, room_b




if __name__ == "__main__":
    rooms = generate_rooms(99,99,50,30)
    print(rooms)
    board = [["."] * 100 for _ in range(100)]
    for room in rooms:
        for i in range(room.lx, room.rx):
            
            board[i][room.ly] = "#"
            board[i][room.ry] = "#"
        for j in range(room.ly, room.ry):
            
            board[room.lx][j] = "#"
            board[room.rx][j] = "#"
        for i in range(room.lx+1, room.rx):
            for j in range(room.ly+1, room.ry):
                board[i][j] = " "

    print("\n".join(" ".join(b) for b in board))




