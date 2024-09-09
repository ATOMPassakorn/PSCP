"""pickThem"""
import json
def pickthem(num_list):
    """pickThem"""
    num_list = json.loads(num_list)
    count = 0
    for i in num_list:
        if not i%2:
            count += 1
            print(i)
    if not count:
        print("Nope")
pickthem(input())
