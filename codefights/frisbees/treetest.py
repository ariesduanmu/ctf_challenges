# -*- coding: utf-8 -*-
from quadtree import QuadTree 
from time import time
from random import randint

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
    print(f"After insert node {time()-start}")
    # return [qt.throwable([i]+points[i]) for i in range(len(points))]
    return [qt.throwable_nosort([i]+points[i]) for i in range(len(points))]

def notree(points):
    distance = lambda f, s: (f[0] - s[0])**2 + (f[1] - s[1])**2
    throwable_points = []
    for s in points:
        reachable_points = [
            (i, distance(f, s))
            for i, f in enumerate(points)
            if s != f and distance(f, s) <= s[2]**2
        ]
        # throwable_points.append([
        #     i for i, _ in sorted(reachable_points, key=lambda i: i[1], reverse=True)
        # ])
        throwable_points.append([
            i for i, _ in reachable_points
        ])
    return throwable_points

def main():
    points = [[randint(0,500), randint(0,500), randint(0,200)] for i in range(5000)]
    start = time()
    tree(points)
    print(f"[+] Time for quadtree {time()-start}")

    start = time()
    notree(points)
    print(f"[+] Time for notree {time()-start}")

if __name__ == "__main__":
    main()

