#!/usr/bin/python3
def best_score(dic):
    if dic and len(dic):
        max = list(dic.keys())[0]
        for key in dic:
            if dic[key] > dic[max]:
                max = key
        return max
    return None
