# -*- coding: utf-8 -*-
from quadtree import QuadTree 
from time import time
from random import randint
import matplotlib.pyplot as plt

def tree(points):
    start = time()
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    x_min, x_max, y_min, y_max = min(x), max(x), min(y), max(y)
    center_x, center_y = (x_min + x_max) / 2, (y_min + y_max) / 2
    width, height = (x_max - x_min) / 2, (y_max - y_min) / 2
    qt = QuadTree((center_x, center_y, width, height), 4)
    for i in range(len(points)):
        qt.insert([i]+points[i])
    # throwable_points = [qt.throwable([i]+points[i]) for i in range(len(points))]
    # print(f"Time used to gather all points without sort { sum(t for _,t in throwable_points)}")
    return [qt.throwable([i]+points[i]) for i in range(len(points))]
    # return [qt.throwable_nosort([i]+points[i]) for i in range(len(points))]

def notree(points):
    distance = lambda f, s: (f[0] - s[0])**2 + (f[1] - s[1])**2
    throwable_points = []
    for s in points:
        reachable_points = [
            (i, distance(f, s))
            for i, f in enumerate(points)
            if s != f and distance(f, s) <= s[2]**2
        ]
        throwable_points.append([
            i for i, _ in sorted(reachable_points, key=lambda i: i[1], reverse=True)
        ])
        # throwable_points.append([
        #     i for i, _ in reachable_points
        # ])
    return throwable_points

def main(n):
    points = [[randint(0,400), randint(0,400), randint(0,500)] for i in range(n)]
    start = time()
    throwable_points = tree(points)
    t1 = time()-start

    start = time()
    throwable_points = notree(points)
    t2 = time()-start

    return t1, t2

if __name__ == "__main__":
    tree_t = []
    notree_t = []

    for _ in range(1000):
        t1,t2 = main(100)
        tree_t.append(t1)
        notree_t.append(t2)
    plt.plot(tree_t, 'r', label="Tree")
    plt.plot(notree_t, 'b', label="NOTree")
    plt.show()

