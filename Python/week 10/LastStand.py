"""laststand"""
import json
def laststand(num_list):
    """laststand"""
    num_list = json.loads(num_list)
    for i in num_list:
        print(str(i)[-1])
laststand(input())
