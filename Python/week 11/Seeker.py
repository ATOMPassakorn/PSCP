"""Seeker"""
def seek():
    """Seeker"""
    text = input()
    num_str=""
    number=[]
    for i in text:
        if i.isdigit():
            num_str+=i
        else:
            if num_str:
                number.append(int(num_str))
                num_str=""
    if num_str:
        number.append(int(num_str))
    print(sum(number))
seek()
