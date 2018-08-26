# -*- coding: utf-8 -*-
import unittest
def gameOfMath(expression):
    expression = expression.split(" ")
    o = set([e for e in expression if not ("0"<=e<="9")])
    if len(o) == 0:
        return expression[0]
    d = {}
    from itertools import permutations
    operations = sorted(list(permutations(o,len(o))))
    for e in operations:
        n = expression
        for i in e: 
            n = afterOperate(i, n)
        for i in range(1,len(e)-1):
            x = "".join(e[:i])
            if x not in d:
                d[x] = [n[0]]
            else:
                d[x].append(n[0])
    print(d)        
    
    return 0

def afterOperate(operate, expression):
    o = {"+":lambda a,b:a+b,
         "-":lambda a,b:a-b,
         "*":lambda a,b:a*b,
         "/":lambda a,b:a//b}
    next_expression = []
    i = 0
    while i < len(expression):
        e = expression[i]
        if e == operate:
            a = next_expression.pop()
            b = expression[i+1]
            next_expression.append(o[e](int(a),int(b)))
            i += 1
        else:
            next_expression.append(e)
        i += 1
    return next_expression

def test():
    expressions = ["7 - 3 * 5 / 2",
                   "5 + 1 - 7 * 2",
                   "7 + 2 * 3 - 5",
                   "5 / 2 - 9 + 2 * 7",
                   "7 - 3 * 5",
                   "5 * 2 * 3 * 6 * 4",
                   "7 / 9 / 4 / 2",
                   "9",
                   "5 - 0 * 3 + 0 * 9 - 5 * 0 + 1",
                   "2 + 3 * 7"]
    for expression in expressions:
        print(f"Expression: {expression}")
        gameOfMath(expression)
        print()
    


class GameOfMathTest(unittest.TestCase):
    def test1(self):
        expression = "7 - 3 * 5 / 2"
        output = 0
        self.assertEqual(gameOfMath(expression), output)

    def test2(self):
        expression = "5 + 1 - 7 * 2"
        output = -8
        self.assertEqual(gameOfMath(expression), output)

    def test3(self):
        expression = "7 + 2 * 3 - 5"
        output = 3
        self.assertEqual(gameOfMath(expression), output)

    def test4(self):
        expression = "5 / 2 - 9 + 2 * 7"
        output = -21
        self.assertEqual(gameOfMath(expression), output)

    def test5(self):
        expression = "7 - 3 * 5"
        output = -8
        self.assertEqual(gameOfMath(expression), output)

    def test6(self):
        expression = "5 * 2 * 3 * 6 * 4"
        output = 720
        self.assertEqual(gameOfMath(expression), output)

    def test7(self):
        expression = "7 / 9 / 4 / 2"
        output = 0
        self.assertEqual(gameOfMath(expression), output)

    def test8(self):
        expression = "9"
        output = 9
        self.assertEqual(gameOfMath(expression), output)

    def test9(self):
        expression = "5 - 0 * 3 + 0 * 9 - 5 * 0 + 1"
        output = 6
        self.assertEqual(gameOfMath(expression), output)

    def test10(self):
        expression = "2 + 3 * 7"
        output = 23
        self.assertEqual(gameOfMath(expression), output)



if __name__ == "__main__":
    # unittest.main()
    test()