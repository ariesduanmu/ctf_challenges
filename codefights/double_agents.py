# -*- coding: utf-8 -*-
'''
LOL I did similiar challenge almost 20 years ago

Full texts of reports are confidential, so your code will get only 
conclusions as an array of booleans: The 0th element is Agent A's 
report on Agent B, the 1st element is Agent B's report on Agent C, 
and so on. true means agent was reported to be clean and false means 
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
        reports = [true, false, false]
        output = "MMM"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_2(self):
        moles = 1
        reports = [true, false, false]
        output = "CCM"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_3(self):
        moles = 2
        reports = [true, false, false]
        output = "M??"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_4(self):
        moles = 1
        reports = [false, true]
        output = "CM"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_5(self):
        moles = 1
        reports = [true, true, true, false]
        output = "MCCC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_6(self):
        moles = 2
        reports = [false, true, true, true]
        output = "CMMC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_7(self):
        moles = 3
        reports = [false, true, false, false]
        output = "?M??"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_8(self):
        moles = 1
        reports = [true, true, false, true, true]
        output = "CCCMC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_9(self):
        moles = 2
        reports = [true, false, true, true, false]
        output = "M??CC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_10(self):
        moles = 3
        reports = [false, false, true, false, true, false]
        output = "??????"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_11(self):
        moles = 4
        reports = [true, false, true, true, false, false, true, false]
        output = "????CM??"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_12(self):
        moles = 3
        reports = [true, true, true, true, true, true, true, true, true, false, false, true, true, true, false, false, true, true, true, true, true, false, true, true, true, true]
        output = "CCCCCCCCCCMCCCCMCCCCCCMCCC"
        self.assertEqual(doubleAgents(moles, reports), output)

    def test_13(self):
        moles = 7
        reports = [true, true, true, true, true, true, false, true, true, true, true, true, true, false, false, false, true, false, true, true, false, false, false, true, true, true]
        output = "CCCCCCCM?CCCCCM??????????C"
        self.assertEqual(doubleAgents(moles, reports), output)


