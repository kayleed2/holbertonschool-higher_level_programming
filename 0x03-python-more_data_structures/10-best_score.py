#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    for k, v in a_dictionary.items():
        if v > score:
            score = v
            high = k
    return high
