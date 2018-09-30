# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2018-09-30 10:06:24
# @Last Modified by:   Li Qin
# @Last Modified time: 2018-09-30 12:06:41

# TODO: this can be a simple game(terminal/GUI)

'''
You have an exam coming up tomorrow morning, 
and you're trying to decide how much longer you should keep studying 
before going to bed. Your uncle, reflecting on his experience in med school, 
once told you that if you have the choice between sleep and study, 
it's always better to get the sleep. But since this is your first semester, 
you suspect you might not be as well prepared for your exams as he would 
have been.

Given the integers familiarity and hoursRemaining, your task is to return 
how many more hours you should study for. familiarity represents 
how confident you are in the material; basically the grade you would 
get if you were to take the exam right now, while hoursRemaining represents 
the number of hours between now and your exam.

Notes:

For every hour you spend studying, you diminish your 'unfamiliarity' 
by 20% (eg: if your familiarity is 70, then your unfamiliarity is 30, 
so after 1 hour of studying, it'll be down to 24, which means your 
familiarity will be 76).
You haven't slept yet, so to be fully alert at the exam, you're depending 
on getting 8 hours of sleep beforehand. If you get fewer than 8 hours, your 
performance will suffer - it's estimated that for every hour less than 8, 
your grade will take a 5 point penalty (eg: with a familiarity of 87, 
if you only sleep 5 hours, then since you're missing 3 hours, your expected 
grade will be 87 - 3 * 5 = 72).
Each hour will be uniquely committed to one activity (studying or sleeping); 
you have a regimented schedule and you'd prefer not to split an hour into \
half study and half sleep.
'''

import unittest
def studyOrSleep(familiarity, hoursRemaining):
    max_familiarity = familiarity
    if hoursRemaining < 8:
        max_familiarity -= 5 * (8-hoursRemaining)
    max_i = 0
    i = 1
    while i <= hoursRemaining:
        unfamiliarity = 100 - familiarity
        familiarity += unfamiliarity * 0.2
        print(familiarity)
        f = familiarity
        if hoursRemaining - i < 8:
            f -= 5 * (8 - hoursRemaining + i)
        if max_familiarity < f:
            max_familiarity = f
            max_i = i
        print(f, i)
        i += 1
    return max_i

class StudyGame(unittest.TestCase):
    def test_1(self):
        familiarity = 64
        hoursRemaining = 8
        output = 2
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_2(self):
        familiarity = 38
        hoursRemaining = 9
        output = 5
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_3(self):
        familiarity = 75
        hoursRemaining = 8
        output = 0
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_4(self):
        familiarity = 87
        hoursRemaining = 11
        output = 3
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_5(self):
        familiarity = 78
        hoursRemaining = 2
        output = 0
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_6(self):
        familiarity = 35
        hoursRemaining = 1
        output = 1
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_7(self):
        familiarity = 77
        hoursRemaining = 18
        output = 10
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_8(self):
        familiarity = 98
        hoursRemaining = 7
        output = 0
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_9(self):
        familiarity = 64
        hoursRemaining = 11
        output = 3
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_10(self):
        familiarity = 48
        hoursRemaining = 0
        output = 0
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_11(self):
        familiarity = 49
        hoursRemaining = 6
        output = 4
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

    def test_12(self):
        familiarity = 70
        hoursRemaining = 3
        output = 1
        self.assertEqual(studyOrSleep(familiarity, hoursRemaining), output)

if __name__ == "__main__":
    unittest.main()
 