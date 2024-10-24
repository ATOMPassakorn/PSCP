"""Flatten"""
import json
def flatten(number):
    """Flatten"""
    result=[]
    for i in number:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
def flat():
    """Flatten"""
    number=json.loads(input())
    ans=flatten(number)
    ans.sort()
    ans.reverse()
    print(ans)
flat()
