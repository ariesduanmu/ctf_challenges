# -*- coding: utf-8 -*-
import unittest
def gameOfMath(expression):
    expression = expression.split(" ")
    possibles = []
    recurse(expression, [], possibles)
    print(possibles)

def recurse(expression, steps, possibles):
    steps.append(expression)
    if len(expression) <= 1:
        possibles.append([steps])
        return
    else:
        for i in range(1,len(expression),2):
            recurse(afterOperate(i, expression), steps, possibles)
def afterOperate(operate_n, expression):
    e = expression[:]
    o = {"+":lambda a,b:a+b,
         "-":lambda a,b:a-b,
         "*":lambda a,b:a*b,
         "/":lambda a,b:a//b}
    r = o[e[operate_n]](int(e[operate_n-1]),int(e[operate_n+1]))
    del e[operate_n-1]
    del e[operate_n-1]
    e[operate_n-1] = r
    return e
    


def test():
    expressions = [
                   "5 - 0 * 3 + 0 * 9 - 5 * 0 + 1",
                   ]
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

    def test11(self):
        expression = "5 + 5 - 2 * 1 - 3 - 2 * 5 * 9"
        output = -37
        self.assertEqual(gameOfMath(expression), output)


if __name__ == "__main__":
    # unittest.main()
    test()