# -*- coding: utf-8 -*-
'''
LOL I did similiar challenge almost 20 years ago

Full texts of reports are confidential, so your code will get only 
conclusions as an array of booleans: The 0th element is Agent A's 
report on Agent B, the 1st element is Agent B's report on Agent C, 
and so on. True means agent was reported to be clean and False means 
agent was reported to be a mole.

Your code should return a string where every character describes the 
alignment of the corresponding agent: `C` for clean, `M` for mole, and `?` 
for unknown.

2 ≤ reports.length ≤ 26
'''
def doubleAgents(moles, reports):
    pass

import unittest

class DoubleAgentsTest(unittest.TestCase):
    def test_1(self):
        moles = 3
        reports = [True, False, False]
        output = "MMM"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_2(self):
        moles = 1
        reports = [True, False, False]
        output = "CCM"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_3(self):
        moles = 2
        reports = [True, False, False]
        output = "M??"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_4(self):
        moles = 1
        reports = [False, True]
        output = "CM"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_5(self):
        moles = 1
        reports = [True, True, True, False]
        output = "MCCC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_6(self):
        moles = 2
        reports = [False, True, True, True]
        output = "CMMC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_7(self):
        moles = 3
        reports = [False, True, False, False]
        output = "?M??"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_8(self):
        moles = 1
        reports = [True, True, False, True, True]
        output = "CCCMC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_9(self):
        moles = 2
        reports = [True, False, True, True, False]
        output = "M??CC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_10(self):
        moles = 3
        reports = [False, False, True, False, True, False]
        output = "??????"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_11(self):
        moles = 4
        reports = [True, False, True, True, False, False, True, False]
        output = "????CM??"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_12(self):
        moles = 3
        reports = [True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True]
        output = "CCCCCCCCCCMCCCCMCCCCCCMCCC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_13(self):
        moles = 7
        reports = [True, True, True, True, True, True, False, True, True, True, True, True, True, False, False, False, True, False, True, True, False, False, False, True, True, True]
        output = "CCCCCCCM?CCCCCM??????????C"
        self.assertEqual(doubleAgents(moles, reports), output)

if __name__ == "__main__":
    unittest.main()