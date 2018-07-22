#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.

def minimumBribes(thisQueue):
    if len(thisQueue) == 1:
        return 0
    else:
        people_that_moved = []
        for ppl in range(1,len(thisQueue)+1):
            if not(ppl == thisQueue[ppl-1]):
                people_that_moved.append(ppl)

        peoples_final_position = []
        for mp in people_that_moved:
            peoples_final_position.append(thisQueue.index(mp) + 1)

        number_of_bribes = 0
        for z in range(len(people_that_moved)):
            movement_value = people_that_moved[z] - peoples_final_position[z]
            if movement_value > 0:
                number_of_bribes += movement_value
            if movement_value > 2:
                return "Too chaotic"
        return number_of_bribes


if __name__ == '__main__':
    t = int(input())
    assert 1 <= t <= 10, "Minimum 1 and maximum 10 test cases are allowed."

    for t_itr in range(t):
        n = int(input())
        assert 1 <= n <= 10 ** 5, "Minimum 1 and maximum 10**5 people are allowed in the queue."

        q = list(map(int, input().rstrip().split()))
        assert len(q) == n, "The amount of entered number does not equal to the initially planned number of people."

        print(minimumBribes(q))
