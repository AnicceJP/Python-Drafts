# Functions for detecting the latest, the best and the top three scores in a raw.

def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]