# -*- coding: utf-8 -*-
import sys
import unittest

def kerstpuzzel(w, d, l, b):
	if (w < l or d < b) and (w < b or d < l):
		return 0 
	# H in bottom left
	i_1, j_1 = box_count(w, l, b)
	i_2, j_2 = box_count(d, b, l)
	if i_1 != 0 and i_2 != 0:
		space_left_1, space_left_2 = place_car_on_left_bottom(w,d,l,b,(l*i_1,b*i_2), j_1, j_2)
		
		(w_1, d_1), c_1 = space_left_1
		box_1 = kerstpuzzel(w_1, d_1, l, b) + c_1 + (i_1*i_2)
		(w_2, d_2), c_2 = space_left_2
		box_2 = kerstpuzzel(w_2, d_2, l, b) + c_2 + (i_1*i_2)
	else:
		box_1 = box_2 = 0

	# V in bottom left

	i_3, j_3 = box_count(w, b, l)
	i_4, j_4 = box_count(d, l, b)
	if i_3 != 0 and i_4 != 0:
		space_left_3, space_left_4 = place_car_on_left_bottom(w,d,l,b,(b*i_3,l*i_4), j_3, j_4, "h")

		(w_3, d_3), c_3 = space_left_3
		box_3 = kerstpuzzel(w_3, d_3, l, b) + c_3 + (i_3*i_4)
		(w_4, d_4), c_4 = space_left_4
		box_4 = kerstpuzzel(w_4, d_4, l, b) + c_4 + (i_3*i_4)
	else:
		box_3 = box_4 = 0
	# return the most car splaced

	box = max([box_1, box_2, box_3, box_4])

	return box


def place_car_on_left_bottom(w, d, l, b, bottomleft, bottom_count, left_count, position="v"):
	width, height = bottomleft
	car_width, car_height = (b, l) if position == "v" else (l, b)

	if bottom_count == 0 and left_count == 0:
		return ((0,0),0), ((0,0),0)
	# 1. over space on bottom side

	if height % car_height:
		bottom_count_1 = height // car_height + 1
	else:
		bottom_count_1 = height // car_height

	if bottom_count_1 * car_height > d:
		bottom_count_1 -= 1

	left_count_1 = width // car_width

	space_left_1 = ((w-(left_count_1*car_width), d-max(height,(bottom_count_1*car_height))), 
		            bottom_count_1*bottom_count + left_count_1*left_count)

	# 2. over space on left side

	if width % car_width:
		left_count_2 = width // car_width + 1
	else:
		left_count_2 = width // car_width

	if left_count_2 * car_width > d:
		left_count_2 -= 1

	bottom_count_2 = height // car_height

	space_left_2 = ((w-max(width,(left_count_2*car_width)), d-(bottom_count_2*car_height)), 
		            bottom_count_2*bottom_count + left_count_2*left_count)

	return space_left_1, space_left_2


def box_count(w, l, b):
	best_l_count = best_b_count = 0
	current_l_count = 1
	best_space_left = w

	while l * current_l_count <= w:
		current_b_count, space_left = divmod(w-(l*current_l_count), b)
		if space_left < best_space_left:
			best_space_left = space_left
			best_l_count = current_l_count
			best_b_count = current_b_count
		current_l_count += 1
	return best_l_count, best_b_count

class KerstpuuzzelTest(unittest.TestCase):
	def test(self):
		w = 42
		d = 39
		l = 9
		b = 4
		output = 45
		self.assertEqual(kerstpuzzel(w,d,l,b),output)

if __name__ == "__main__":
    # kerstpuzzel(*sys.argv[1:5])
    print(kerstpuzzel(42, 39, 9, 4))

