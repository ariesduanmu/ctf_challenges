# -*- coding: utf-8 -*-
# I stealed this solution because it is so great
'''
Given the expression in the form of a string, 
your task is to find the best (minimal) result you can achieve, 
assuming both players make optimal choices.
'''
import unittest
from cProfile import Profile
from pstats import Stats
import tracemalloc

d = {}
def gameOfMath(expression):
    global d
    expression = expression.split(" ")
    numbers = [int(expression[i]) for i in range(len(expression)) if i % 2 == 0]
    operators = [expression[i] for i in range(len(expression)) if i % 2 == 1]
    d = {}
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

def gameOfMath_d(expression):
    expression = expression.split(" ")
    numbers = [int(expression[i]) for i in range(len(expression)) if i % 2 == 0]
    operators = [expression[i] for i in range(len(expression)) if i % 2 == 1]
    return numbers[0] if len(operators) == 0 else progress_d(numbers, operators, True)

def progress_d(numbers, operators, me):
    global d
    k = ",".join(list(map(str, numbers)) + operators)
    if k not in d:
        d[k] = 1
    else:
        return d[k]
    fO = operation(numbers[0], numbers[1], operators[0])
    if len(operators) == 1:
        return fO

    e = progress_d([fO] + numbers[2:], operators[1:], not me)

    for i in range(1, len(operators)):
        n = operation(numbers[i], numbers[i+1], operators[i])
        v = progress_d(numbers[:i] + [n] + numbers[i+2:], operators[:i]+operators[i+1:], not me)
        if (v > e) != me:
            e = v
    d[k] = e
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

def expressions():
    return ["7 - 3 * 5 / 2",
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

def profile_test():
    for expression in expressions():
        print(f"Expression: {expression}")
        profiler = Profile()
        profiler.runcall(gameOfMath, expression)
        stats = Stats(profiler)
        stats.strip_dirs()
        stats.sort_stats('cumulative')
        stats.print_stats()
        print()
        profiler = Profile()
        profiler.runcall(gameOfMath_d, expression)
        stats = Stats(profiler)
        stats.strip_dirs()
        stats.sort_stats('cumulative')
        stats.print_stats()
        print()

def malloc_test():
    for expression in expressions():
        tracemalloc.start(3)
        time1 = tracemalloc.take_snapshot()
        gameOfMath_d(expression)
        time2 = tracemalloc.take_snapshot()
        stats = time2.compare_to(time1, 'lineno')
        for stat in stats:
            print(stat)
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
    # profile_test()
    malloc_test()




