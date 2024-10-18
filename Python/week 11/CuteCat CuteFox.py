'''find cat and fox'''
import json
def alphanum_key(s):
    '''check digit'''
    num = ''
    parts = []
    for char in s:
        if char.isdigit():
            num += char
        else:
            if num:
                parts.append(int(num))
                num = ''
            parts.append(char)
    if num:
        parts.append(int(num))
    return parts

def main():
    '''main'''
    my_dict = {}
    result = {}
    cat_count = 0
    fox_count = 0
    text = ""
    n = int(input())
    for _ in range(n):
        name = input()
        find_colon = name.find(':')
        length = len(name)
        for i in range(length):
            if i in (1, find_colon - 2, find_colon + 2, len(name) - 2):
                text += "\""
            else:
                text += str(name[i])
        my_dict.update(json.loads(text))
        text = ""
    if 'Garfield' not in my_dict and 'Cat01' not in my_dict.values():
        my_dict.update({'Garfield': 'Cat01'})
    if 'Fubuki' not in my_dict and 'Fox01' not in my_dict.values():
        my_dict.update({'Fubuki': 'Fox01'})
    for _, y in my_dict.items():
        if 'Cat' in y:
            cat_count += 1
        if 'Fox' in y:
            fox_count += 1
    new_dict = sorted(my_dict.values(), key=alphanum_key)
    for x in new_dict:
        for z in my_dict.items():
            if z[1] == x:
                result.update({z[0]: x})
                break
    print(f'Cat : {cat_count}', f'Fox : {fox_count}', sep='\n')
    return result
result_1 = main()
def printtt():
    '''eeee'''
    for m, n in result_1.items():
        print(f'{m} : {n}')
printtt()
