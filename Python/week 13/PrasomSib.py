"""PrasomSib"""
def ten():
    """PrasomSib"""
    number=input()
    digit=[int(i) for i in number]
    count = 0
    length = len(digit)
    for start in range(length):
        current_sum = 0
        for end in range(start,length):
            current_sum += digit[end]
            if current_sum==10:
                count+=1
    print(count)
ten()
