# -*- coding: utf-8 -*-
class QuadTree():
    def __init__(self, boundry, capacity):
        self.boundry = boundry
        self.capacity = capacity
        self.nodes = []
        self.subquads = []
        self.divised = False

    def insert(self, point):
        if not self._inrange(point):
            return False
        if len(self.nodes) < self.capacity:
            self.nodes.append(point)
        else:
            if not self.divised:
                self._divisional()
                self.divised = True
            for child in self.subquads:
                if child.insert(point):
                    break
        return True

    def query(self, circle):
        points = []
        idx, x,y,r = circle
        if self._intersect(circle):
            for node in self.nodes:
                i,a,b,_ = node
                d = (r ** 2) -  ((a-x) ** 2 + (b-y) ** 2)
                if i != idx and d >= 0:
                    points += [[node[0], d]]
            
            if self.divised:
                for child in self.subquads:
                    points += child.query(circle)
        return points

    def throwable(self, circle):
        points = self.query(circle)

        return [i for i,_ in sorted(points, key=lambda x:x[1])]

    def _divisional(self):
        x, y, w, h = self.boundry
        self.subquads = [QuadTree((x-w/2, y-h/2, w/2, h/2), self.capacity),
                         QuadTree((x-w/2, y+h/2, w/2, h/2), self.capacity),
                         QuadTree((x+w/2, y-h/2, w/2, h/2), self.capacity),
                         QuadTree((x+w/2, y+h/2, w/2, h/2), self.capacity)]

    def _intersect(self, circle):
        x, y, w, h = self.boundry
        _, a, b, r = circle
        a -= x
        b -= y
        dx = max(min(a, w), -w)
        dy = max(min(b, h), -h)
        return (dx-a) ** 2 + (dy-b) ** 2 <= r ** 2


    def _inrange(self, point):
        x, y, w, h = self.boundry
        _, a, b, _ = point
        if x-w <= a <= x+w and y-h <= b <= y+h:
            return True
        return False

    def allpoints(self):
        s = []
        for idx, x, y, r in self.nodes:
            s += [f"[{idx}] ({x}, {y}) {r}"]
        if self.divised:
            for child in self.subquads:
                s += child.allpoints()
        return s

    def __str__(self):
        return "\n".join(self.allpoints())



if __name__ == "__main__":
    friends  = [[152,213,276], 
               [274,259,151], 
               [40,57,130], 
               [203,87,189], 
               [43,182,163]]
    numberOfPasses = 19
    startingPlayer = 4
    frisbees(friends, numberOfPasses, startingPlayer)

