# -*- coding: utf-8 -*-
# I stealed this solution because it is so great
'''
Given the expression in the form of a string, 
your task is to find the best (minimal) result you can achieve, 
assuming both players make optimal choices.
'''


import unittest
def gameOfMath(expression):
    expression = expression.split(" ")
    numbers = [int(expression[i]) for i in range(len(expression)) if i % 2 == 0]
    operators = [expression[i] for i in range(len(expression)) if i % 2 == 1]
    return numbers[0] if len(operators) == 0 else progress(numbers, operators, True)

def progress(numbers, operators, me):
    fO = operation(numbers[0], numbers[1], operators[0])
    if len(operators) == 1:
        return fO

    e = progress([fO] + numbers[2:], operators[1:], not me)

    for i in range(1, len(operators)):
        n = operation(numbers[i], numbers[i+1], operators[i])
        v = progress(numbers[:i] + [n] + numbers[i+2:], operators[:i]+operators[i+1:], not me)
        if (v > e) != me:
            e = v
    return e

def operation(a, b, o):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "*":
        return a * b
    elif o == "/":
        return a // b

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
                   "2 + 3 * 7",
                   "5 + 5 - 2 * 1 - 3 - 2 * 5 * 9"]
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
    unittest.main()
    # test()