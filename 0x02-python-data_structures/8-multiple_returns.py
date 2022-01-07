#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        newtup = len(sentence), None
        return newtup
    else:
        newtup = len(sentence), sentence[0]
        return newtup