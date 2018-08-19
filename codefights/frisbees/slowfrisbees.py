# -*- coding: utf-8 -*-
def distance(f, s):
    return (f[0] - s[0])**2 + (f[1] - s[1])**2

def make_player_throws_list(friends):
    throwable_friends = []
    for s in friends:
        reachable_friends = [
            (i, distance(f, s))
            for i, f in enumerate(friends)
            if s != f and distance(f, s) <= s[2]**2
        ]
        throwable_friends.append([
            i for i, _ in sorted(reachable_friends, key=lambda i: i[1], reverse=True)
        ])
    return throwable_friends

def frisbees(friends, number_of_passes, player):
    frisbee_held = {i: 0 for i in range(len(friends))}
    throwable_friends = make_player_throws_list(friends)
    
    for _ in range(number_of_passes):
        frisbee_held[player] += 1
        player = min(throwable_friends[player], key=frisbee_held.get)
    return player

if __name__ == "__main__":
    friends = [[119,356,361], 
               [1,106,238], 
               [222,101,346], 
               [6,375,360], 
               [62,369,97], 
               [356,44,150], 
               [371,209,403], 
               [225,29,295], 
               [49,8,429], 
               [334,175,427]]
    numberOfPasses = 499
    startingPlayer = 6
    frisbees(friends, numberOfPasses, startingPlayer)
