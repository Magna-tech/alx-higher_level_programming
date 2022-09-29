#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        i = max(a_dictionary.keys(), key=(lambda k: a_dictionary[k]))
        return i
